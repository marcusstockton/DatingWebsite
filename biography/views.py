import os

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import ListView
from formtools.wizard.views import SessionWizardView

from .filters import ProfileFilter
from .forms import RegisterForm, ProfileForm, AddressForm, ProfileEditForm
from .models import Profile, Images


class ProfileListView(ListView):
    model = Profile
    template_name = 'biography/index.html'
    context_object_name = 'latest_profiles'
    ordering = ['-created_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProfileFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        # exclude the logged in user...they don't need to see themselves in the results.
        if self.request.user.is_authenticated:
            return qs.exclude(user_id=self.request.user)
        else:
            return qs


def detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    images = Images.objects.filter(profile_id=pk)
    return render(request, 'biography/detail.html', {'profile': profile, "images": images})


def user_create(request):
    form = RegisterForm(request.POST or None, request.FILES or None)
    profile = ProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid() and profile.is_valid():
        user = form.save()
        profile = profile.save(commit=False)
        profile.user = user
        profile.save()
        auth_user = authenticate(username=user.username, password=user.password)
        login(request, user)
        return redirect("biography:index")
    context = {
        "form": form,
        "profile": profile
    }
    return render(request, "create.html", context)


# keeping this and detail in, as i'll likely want less info on detail, more in this..
def account_profile(request):
    user_id = request.user.id
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    images = Images.objects.filter(profile_id=user_id)

    return render(request, 'biography/my_account.html', {'profile': profile, "images": images})


class EditView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'biography/edit_my_account.html'


class UserCreationWizard(SessionWizardView):
    form_list = [RegisterForm, ProfileForm, AddressForm]
    template_name = "register_user.html"
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'ProfilePics_temp'))

    def done(self, form_list, form_dict, **kwargs):
        register_form = form_dict['0']
        profile_form = form_dict['1']
        address_form = form_dict['2']
        with transaction.atomic():
            user = register_form.save()
            address = address_form.save()
            profile = profile_form.save(commit=False)
            profile.address = address
            profile.user = user
            profile.save()
            login(self.request, user)
            return redirect('biography:my-profile')
