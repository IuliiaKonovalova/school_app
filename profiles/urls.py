from django.urls import path
from .views import UserProfileView


urlpatterns = [
    path('<slug:phone>/', UserProfileView.as_view(), name='user_profile'),
]
