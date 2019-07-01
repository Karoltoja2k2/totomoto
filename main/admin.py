from django.contrib import admin

# Register your models here.

from .models import Offer, Images

admin.site.register(Offer)
admin.site.register(Images)