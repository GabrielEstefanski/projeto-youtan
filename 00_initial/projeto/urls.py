"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views

STATIC_ROOT = "projeto/static/"

admin.autodiscover()

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path(r'^$', TemplateView.as_view(template_name='home.html'), name='base'), 
    path("home/", views.empresaList.as_view(template_name='campo.html'), name='start'),
    path('home/cadastrar/empresa/', views.empresaCreate.as_view(), name="cadastrar-empresa"),
    path('home/editar/<int:pk>', views.empresaUpdate.as_view(), name='editar-empresa'),
    path('home/excluir/<int:pk>/', views.empresaDelete.as_view(template_name='form-excluir.html'), name='excluir-empresa'),
    path('', views.cnpjCreate, name='cnpjCreate')
      
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 