from django.shortcuts import render, get_object_or_404
from .models import Band
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """
    View function to render the home page of the band app.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'homeband.html' template.
    """
    return render(request, 'band/homeband.html')


@login_required(login_url="user_auth:login")
def band_list(request):
    """
    View function to list all the bands.

    Only accessible to logged-in users. Displays a list of all the bands
    from the database.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'bandlist.html' template with the list of bands.
    """
    list_of_bands = Band.objects.all()
    context = {'list_of_bands': list_of_bands}
    return render(request, 'band/bandlist.html', context)


def band_detail(request, pk):
    """
    View function to display the details of a specific band.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the band to retrieve.

    Returns:
        HttpResponse: The rendered 'bandDetail.html' template with the band details.
    """
    band = get_object_or_404(Band, pk=pk)
    context = {'band': band}
    return render(request, 'band/bandDetail.html', context)
