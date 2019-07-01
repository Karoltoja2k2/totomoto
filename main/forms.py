from django.forms import ModelForm
from .models import Offer, Images

class NewOffer(ModelForm):

    class Meta:
        model = Offer
        fields = ('title', 'mm', 'accident', 'price', )


class ImageForm(ModelForm):

    class Meta:
        model = Images
        fields = ('image', )