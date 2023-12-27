from .models import Page
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import CrearPagina
from django.shortcuts import get_object_or_404

# Create your views here.
class PagesListView(ListView):
    model = Page

class PagesDetailView(DetailView):
    model = Page
    
class PagesCreateView(CreateView):
    model = Page
    form_class = CrearPagina
    template_name = 'pages/create_form.html'
    success_url = reverse_lazy('pages') 
    
class PagesUpdateView(UpdateView):
    model = Page
    form_class = CrearPagina
    template_name = 'pages/update_form.html'
    success_url = reverse_lazy('pages') 
    
class PagesDeleteView(DeleteView):
    model = Page
    template_name = 'pages/delete_form.html'
    success_url = reverse_lazy('pages') 
    def get_object(self, queryset=None):
        # Sobrescribe el método para obtener el objeto a eliminar
        pk = self.kwargs.get('pk')
        return get_object_or_404(Page, pk=pk)