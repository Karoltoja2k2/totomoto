from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.offer, name='offer'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('bye/', views.bye, name='bye'),
    path('uoffer/', views.uoffer, name='uoffer'),
    path('uoffer/<int:id>', views.uoffer, name='uoffer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)