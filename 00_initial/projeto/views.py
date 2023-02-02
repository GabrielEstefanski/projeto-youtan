from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import Cnpj
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy

from projeto.crm.models import *

DIR_LIST = "C:/Users/R31_d0_R0CK/Desktop/projeto-python/00_initial/projeto/templates/"

class empresaCreate(CreateView):
   model = Empresa
   fields = ['nome','ativo']
   template_name = DIR_LIST + 'form.html'
   success_url = reverse_lazy('start')

class empresaList(ListView):
   model = Empresa
   template_name = DIR_LIST + 'campo.html'
   paginate_by = 10

   def get_queryset(self):
      txt_nome = self.request.GET.get('nome')
      if txt_nome:
         empresas = Empresa.objects.filter(nome__icontains=txt_nome)
      else:
         empresas = Empresa.objects.all()

      return empresas

class empresaUpdate(UpdateView):
   model = Empresa
   fields = ['nome','ativo']
   template_name = DIR_LIST + 'form.html'
   success_url = reverse_lazy('start') 

class empresaDelete(DeleteView):
   model = Empresa
   template_name = DIR_LIST + 'form.html'
   success_url = reverse_lazy('start') 

def home(request):
   form = Cnpj()
   return render(request, 'form.html', {'form':form})
 
def cnpjCreate(request):
   form = Cnpj(request.POST)
   if form.is_valid():
      form.save()
      return HttpResponse("Salvo com sucesso")
   return HttpResponse("Erro")


