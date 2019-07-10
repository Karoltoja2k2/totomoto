from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.offer, name='offer'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('user/', views.user_offs, name='user_offs'),
    path('user/<str:name>/', views.user_offs, name='user_offs'),
    path('edit/<int:id>/', views.edit_offer, name='edit_offer'),
    path('user_info/', views.user_info, name='user_info'),

    path('bye/', views.bye, name='bye'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)