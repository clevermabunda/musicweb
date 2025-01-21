from django.urls import path
from . import views
from .views import SignUpView

app_name = 'user_auth'

urlpatterns = [
    # URL pattern for the login page. It renders the 'login.html' template.
    path('', views.user_login, name='login'),

    # URL pattern for showing the logged-in user's details (username and password).
    path('show_user/', views.show_user, name='show_user'),

    # URL pattern for authenticating the user using the 'authenticate_user' view.
    # It processes the login form and redirects based on whether the user is authenticated or not.
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),

    # URL pattern for the sign-up page, handled by the SignUpView class-based view.
    # This renders the user creation form and redirects to login after successful sign-up.
    path("signup/", SignUpView.as_view(), name="signup"),
]
