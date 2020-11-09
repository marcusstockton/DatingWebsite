import os
from datetime import datetime

from django.conf import settings
from django.db import models
from shared.enums import Title, Gender, BodyType


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/ProfilePics/user_<id>/<filename>
    return 'ProfilePics/user_{0}/{1}'.format(instance.pk, filename)


def user_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/ProfilePics/user_<id>/<filename>
    return 'ProfilePics/user_{0}/{1}'.format(instance.profile.pk, filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # bind profile to user model.
    title = models.CharField(max_length=10, choices=Title.choices())
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=5, choices=Gender.choices())
    interested_in = models.CharField(max_length=2, choices=Gender.choices())
    address = models.OneToOneField("Address", on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=user_directory_path)
    body_shape = models.CharField(max_length=3, choices=BodyType.choices())
    title = models.CharField(max_length=200, help_text="A title to make you stand out.")
    description = models.CharField(max_length=2000, help_text="Describe yourself.")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    @property
    def age(self):
        return int((datetime.now().date() - self.dob).days / 365.25)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Address(models.Model):
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, blank=True, null=True)
    post_code = models.CharField(max_length=8)
    city = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return "{} {} {} {}".format(self.line1, self.line2, self.post_code, self.city)


class Images(models.Model):
    image = models.ImageField(upload_to=user_image_path, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return "{} {} {}".format(os.path.basename(self.image.file.name), self.profile.first_name, self.profile.last_name)