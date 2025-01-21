from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def user_login(request):
    """
    Renders the login page for the user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'login.html' template.
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Authenticates a user based on the username and password from the login form.

    Args:
        request (HttpRequest): The HTTP request object containing the login form data.

    Returns:
        HttpResponseRedirect: Redirects to either the login page or the band list based on authentication success.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('band_list'))

def show_user(request):
    """
    Displays the username and password of the logged-in user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'user.html' template with the user's information.
    """
    print(request.user.username)  # Prints the username to the console (for debugging purposes)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

class SignUpView(generic.CreateView):
    """
    A view for user sign-up.

    Inherits from Django's generic `CreateView` to handle user registration using the `UserCreationForm`.
    After successful sign-up, the user is redirected to the login page.

    Attributes:
        form_class (UserCreationForm): The form class used for user registration.
        success_url (reverse_lazy): The URL to redirect to after successful sign-up.
        template_name (str): The template to render for the sign-up page.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "authentication/signup.html"
