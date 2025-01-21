from django.db import models

# Create your models here.

class Band(models.Model):
    """
    Model representing a music band.

    Attributes:
        band_name (str): The name of the band.
        number_of_members (int): The number of members in the band.
        year_formed (date): The year when the band was formed.
        genre (str): The genre of music the band plays.
        about_the_band (str, optional): A detailed description of the band (optional).

    Methods:
        __str__(): Returns the band name when the object is represented as a string.
    """
    
    band_name = models.CharField(max_length=50)
    number_of_members = models.IntegerField()
    year_formed = models.DateField()
    genre = models.CharField(max_length=50)
    about_the_band = models.CharField(max_length=10000, null=True)

    def __str__(self) -> str:
        """
        Returns the name of the band when the object is represented as a string.

        Returns:
            str: The band's name.
        """
        return self.band_name
