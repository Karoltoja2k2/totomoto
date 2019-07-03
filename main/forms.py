from django.forms import ModelForm
from django import forms
from .models import Offer, Images

class NewOffer(ModelForm):


    class Meta:
        model = Offer
        fields = ('title', 'dsc', 'category', 'marka', 'model', 'type', 'stan',
                  'prod_year', 'mileage', 'cap', 'fuel', 'power', 'gear_box',
                  'colour', 'accident', 'price'
                  )

        labels = {'title':'Tytuł oferty', 'dsc':'Opis', 'category':'Kategoria',
                  'marka':'Marka', 'model':'Model', 'type':'Typ nadowzia',
                  'stan':'Używany', 'prod_year':'Rok produkcji', 'mileage':'Przebieg',
                  'cap':'Pojemność silnika', 'fuel':'Rodzaj paliwa', 'power':'Moc',
                  'gear_box':'Skrzynia biegów', 'colour':'Kolor', 'accident':'Bezwypadkowy',
                  'price':'Cena'
                  }



        #widgets = {
        #    'title': forms.TextInput(attrs={'class': 'form-control'}),
        #}


class ImageForm(ModelForm):

    class Meta:
        model = Images
        fields = ('image', )

        labels = {'image':'' , }