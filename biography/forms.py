from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, fields, DateInput

from .models import Profile, Address


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AddressForm(ModelForm):

    class Meta:
        model = Address
        fields = "__all__"


class ProfileForm(ModelForm):
    dob = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Profile
        exclude = ['user', 'address', 'created_date', 'updated_date']


class ProfileEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['address'].widget.attrs['disabled'] = True
        self.fields['user'].widget.attrs['disabled'] = True
        self.fields['dob'].widget = DateInput(attrs={'type': 'date'})
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 6, 'cols': 15})

    class Meta:
        model = Profile
        fields = "__all__"
