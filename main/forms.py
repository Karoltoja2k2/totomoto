from django.forms import ModelForm
from django import forms
from .models import Offer, Images
from .models import Category, CarMark, Stan, Status, Type, Fuel, GearBox, Naped
import datetime
from .choices import *
from multiselectfield import MultiSelectField



today = datetime.date.today().year


class NewOffer(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Kategoria')
    marka = forms.ModelChoiceField(queryset=CarMark.objects.all())
    stan = forms.ModelChoiceField(queryset=Stan.objects.all(), label='Stan')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status pojazdu')

    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Typ nadwozia')
    fuel = forms.ModelChoiceField(queryset=Fuel.objects.all(), label='Rodzaj paliwa')
    gear_box = forms.ModelChoiceField(queryset=GearBox.objects.all(), label='Skrzynia biegów')
    naped = forms.ModelChoiceField(queryset=Naped.objects.all(), label='Rodzaj napędu')


    prod_year = forms.IntegerField(min_value=1900, max_value=today, label='Rok produkcji')


    class Meta:
        model = Offer
        fields = ('title', 'dsc', 'category', 'marka', 'model', 'type', 'stan',
                  'prod_year', 'mileage', 'cap', 'fuel', 'power', 'gear_box',
                  'naped', 'colour', 'status', 'price'
                  )

        labels = {'title':'Tytuł oferty', 'dsc':'Opis', 'category':'Kategoria',
                  'marka':'Marka', 'model':'Model', 'type':'Typ nadowzia',
                  'stan':'Używany', 'prod_year':'Rok produkcji', 'mileage':'Przebieg',
                  'cap':'Pojemność silnika', 'fuel':'Rodzaj paliwa', 'power':'Moc',
                  'gear_box':'Skrzynia biegów', 'colour':'Kolor', 'status':'Bezwypadkowy',
                  'price':'Cena'
                  }



        #widgets = {
        #    'title': forms.TextInput(attrs={'class': 'form-control'}),
        #}

class SearchOff(forms.Form):
    #category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Kategoria', required=False)
    marka = forms.ModelChoiceField(queryset=CarMark.objects.all(), required=False)
    #model = forms.CharField(max_length=30, required=False)
    #type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False)

    # stan = forms.ModelChoiceField(queryset=Stan.objects.all(), required=False)
    # prod_year_min = forms.IntegerField(required=False)
    # prod_year_max = forms.IntegerField(required=False)
    # mileage_min = forms.IntegerField(required=False)
    # mileage_max = forms.IntegerField(required=False)
    # cap_min = forms.IntegerField(required=False)
    # cap_max = forms.IntegerField(required=False)
    fuel = forms.MultipleChoiceField(choices=FUEL, widget=forms.CheckboxSelectMultiple(), required=False)
    #price_min = forms.IntegerField(required=False)
    #price_max = forms.IntegerField(required=False)


    class Meta:
        model = Offer
        fields = (
                  )


class ImageForm(ModelForm):

    class Meta:
        model = Images
        fields = ('image', )

        labels = {'image':'', }