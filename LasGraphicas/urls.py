"""
URL configuration for LasGraphicas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from LasGraphicas import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('polos/', views.polos, name='polos'),
    path('add_to_wishlist/<uuid:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('round-neck/', views.roundNeck, name='round'),
    path('polos/<uuid:id>', views.detail, name= 'singleProduct'),
    path('privacy-policy/', views.privacyPolicy, name= 'privacy_policy'),
    path('exchange-and-returns/', views.exchangeAndReturns, name= 'exchange-returns'),
    path('contact/', views.contact_us, name= 'contact_us'),
    path('policy/', views.policy, name= 'terms'),
    path('update-product/<str:pk>/', views.updateProduct, name= 'updateProduct'),
    path('delete-product/<str:pk>/', views.deleteProduct, name= 'deleteProduct'),
    path('users/', include('users.urls')),
    path('wishlist/', views.view_wishlist, name= 'wishlist'),
    path('search/', views.searchPage, name= 'search'),
    path('about-us/', views.aboutUs, name= 'about-us'),
    path('shipping/', views.shipping, name= 'shipping'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)