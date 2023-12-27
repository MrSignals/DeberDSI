from django.urls import path
from .views import PagesListView, PagesDetailView, PagesCreateView,PagesUpdateView,PagesDeleteView

urlpatterns = [
    path('list/', PagesListView.as_view(), name='pages'),
    path('create/', PagesCreateView.as_view(), name='crearPages'),
    path('<int:pk>/update/', PagesUpdateView.as_view(), name='page_update'),
    path('<int:pk>/delete/', PagesDeleteView.as_view(), name='page_delete'),
    path('<int:pk>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
    
]