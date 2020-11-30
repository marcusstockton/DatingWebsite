from django.urls import path

from . import views
from .views import ProfileListView

app_name = 'biography'
urlpatterns = [
    path('', ProfileListView.as_view(), name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('register', views.UserCreationWizard.as_view(), name='register'),
    path('view-my-profile', views.account_profile, name='my-profile')
]