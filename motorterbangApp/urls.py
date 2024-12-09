from django.urls import path
from . import views
from .views import dynamic_scrape_view

app_name = "motorterbangApp"
urlpatterns = [
    path('barang/', views.IndexView.as_view(), name='daftar_barang'),
    path('', views.index, name='index'),
    path('scrape/', dynamic_scrape_view, name='dynamic_scrape'),
    path("barang/tambah-barang/", views.tambahBarang, name="tambah_barang"),
    path("barang/<pk>/", views.DetailView.as_view(), name="detail_barang"),
    path("barang/<pk>/edit/", views.editBarang, name="edit_barang"),  
]