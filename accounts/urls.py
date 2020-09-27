from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SubmittableLoginView, SubmittableMessagedLogoutView, SubmittablePasswordChangeView, SignUpView


app_name = 'accounts'
urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', SubmittableMessagedLogoutView.as_view(), name='logout'),
    path('password_change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('registration/', SignUpView.as_view(), name='registration'),
]
