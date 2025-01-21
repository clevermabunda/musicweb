from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    """
    The home URL pattern, which renders the home page of the band app.
    This view will load the 'homeband.html' template.
    """
    
    path('band_list/', views.band_list, name='band_list'),
    """
    The URL pattern to display the list of all bands. 
    It is associated with the 'band_list' view, which renders 
    the 'bandlist.html' template, showing a list of all bands.
    The view is protected by the login_required decorator.
    """
    
    path('<int:pk>/', views.band_detail, name='band_detail'),
    """
    The URL pattern for displaying a specific band's details.
    The 'pk' (primary key) is passed to the 'band_detail' view to fetch and render
    details of the specific band using the 'bandDetail.html' template.
    """
]
