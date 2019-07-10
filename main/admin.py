from django.contrib import admin

# Register your models here.

from .models import Offer, Images, Userinf, Category, CarMark, Stan, Status, Type, Fuel, GearBox, Naped

admin.site.register(Offer)
admin.site.register(Images)
admin.site.register(Userinf)
admin.site.register(CarMark)
admin.site.register(Category)
admin.site.register(Stan)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Fuel)
admin.site.register(GearBox)
admin.site.register(Naped)
