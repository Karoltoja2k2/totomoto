from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.offer, name='offer'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('user/<str:name>/', views.user_offs, name='user_offs'),
    path('user_info/', views.user_info, name='user_info'),
    path('uoffer/', views.your_offers, name='uoffer'),
    path('uoffer/<int:id>', views.your_offers, name='uoffer'),
    path('bye/', views.bye, name='bye'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)