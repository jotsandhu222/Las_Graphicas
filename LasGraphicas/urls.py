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
    path('tshirts/', views.tshirts, name='tshirts'),
    path('', views.home, name='home'),  
    path('polos/', views.polos, name='polos'),
    path('polos/<int:id>', views.detail),
    path('polos/add', views.add),
    path('privacy-policy/', views.privacyPolicy, name= 'privacy_policy'),
    path('exchange-and-returns/', views.exchangeAndReturns, name= 'exchange_returns'),
    path('contact/', views.contact_us, name= 'contact_us'),
    path('cancellation-policy/', views.cancellationPolicy, name= 'cancellation_policy')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)