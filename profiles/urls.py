from django.urls import path
from .views import UserProfileView, UserProfileEditView


urlpatterns = [
    path('<slug:phone>/', UserProfileView.as_view(), name='user_profile'),
    path('<slug:phone>/edit/', UserProfileEditView.as_view(), name='user_profile_edit'),
    path('<slug:phone>/applications/', UserProfileView.as_view(), name='new_applications'),
    path('<slug:phone>/applications/<int:pk>/', UserProfileView.as_view(), name='application_detail'),
]
