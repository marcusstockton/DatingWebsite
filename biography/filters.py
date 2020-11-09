import django_filters

from biography.models import Profile


class ProfileFilter(django_filters.FilterSet):

    class Meta:
        model = Profile
        fields = ('interested_in', 'body_shape')