from django.urls import path

from .views import SignUpView, ProfileView, ChangeProfileView

urlpatterns = [

    path('signup/,', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ChangeProfileView.as_view(), name='profile_edit'),

]