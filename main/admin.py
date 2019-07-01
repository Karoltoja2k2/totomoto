from django.contrib import admin

# Register your models here.

from .models import Offer, Images, Userinf

admin.site.register(Offer)
admin.site.register(Images)
admin.site.register(Userinf)