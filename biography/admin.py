from django.contrib import admin
from django import forms
from .models import Profile, Address, Images


class ImageProfileInline(admin.TabularInline):
    model = Images


class ProfileModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileModelForm
    inlines = (ImageProfileInline,)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(Images)
