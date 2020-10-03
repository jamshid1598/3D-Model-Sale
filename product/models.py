from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


User = get_user_model()

# Create your models here.

class Category_3D(models.Model):
    category_name = models.CharField( max_length = 200, verbose_name = "Kategoriya nomi", unique=True )

    class Meta:
        ordering            = ['category_name']
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.category_name


class Modul_Format_3D(models.Model):
    modul_constructor = models.CharField(max_length =100, verbose_name = 'Konstruktor Dasturlar', unique = True )
    modul_extension   = models.CharField(max_length = 10, verbose_name = 'Modul Farmati', blank = True, null = True)
    class Meta:
        ordering = [
            'modul_constructor'
        ]
        verbose_name_plural = 'Konstruktor Dasturlar'

    def __str__(self):
        return "{} - {}".format(self.modul_constructor, self.modul_extension)
    


class Info_Modul_3D(models.Model):

    modul_file        = models.FileField( verbose_name = '3D Modul Fayli', upload_to = 'moduls/%Y/%m/%d/') # uploaded file is stored in 'MEDIA_ROOT/moduls/YYYY/MM/DD/' folder
    modul_images      = models.ImageField( verbose_name = '3D Modul Rasmi', upload_to = 'images/')
    modul_name        = models.CharField( max_length = 300, verbose_name = "3D Modul Nomi" )
    modul_description = models.TextField( verbose_name = 'Tarif' )
    modul_price       = models.DecimalField( verbose_name = '3D Modul Narxi', max_digits = 10, decimal_places = 2, default = 0,
                            validators=(
                                MinValueValidator(0),
                                MaxValueValidator(100000000),
                            )
                        )
    
    # Class for choosing currency type 
    class CurrecyChoice(models.TextChoices):
        SUM="so\'m",_('so\'m')
        USD='$',_('dollor')
        EUR='euro',_('euro')
        RUB='ruble',_('ruble')
        __empty__=_('')
    price_currency    = models.CharField( max_length = 50, verbose_name = 'Valyuta Turi', 
                            choices = CurrecyChoice.choices, 
                            default = CurrecyChoice.__empty__ 
                        )
    modul_format      = models.ManyToManyField(Modul_Format_3D)

    state_active      = models.BooleanField( default = True )
    modul_animated    = models.BooleanField( default = False )
    modul_printable   = models.BooleanField( default = False )

    modul_primary_category     = models.ForeignKey( Category_3D, on_delete=models.SET_NULL, 
                                    related_name = 'modul_primary_category', 
                                    blank        = True, 
                                    null         = True 
                                )
    modul_secondary_categories = models.ManyToManyField(Category_3D, related_name = 'modul_secondary_category' )

    modul_author_name = models.CharField( max_length = 150, verbose_name = "Muallif ismi" )
    modul_published   = models.DateTimeField( auto_now_add =True )
    modul_updated     = models.DateTimeField( auto_now = True )

    class Meta:
        ordering = [
            'modul_published',
            'modul_updated',
        ]
        verbose_name        = '3D Modul Malumotlari'
        verbose_name_plural = '3D Modul Malumotlari'


    def __str__(self):
        return "{} - by: {}".format(self.modul_name, self.modul_author_name)

"""

Category_3D :
    name


Product_Format:
    name,
    year                 = PI (choice)



Info_Model_3D:
    name,
    slug,
    description,
    author_name,
    price,
    currency             = CHF (choices)
    published_date,
    updated_date,
    format               = MTM, or smth else like checkbox
    animated              BF (default = False)
    printable_3d         = BF (default = False)  
    active               = BF (default = True),

    primary_category     = FK,
    secondary_categories = MTM,


"""