from typing import Any
from django.db.models import F
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.http import JsonResponse
import uuid
from .forms import BarangForm
from .models import Barang
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from .utils.scraper import scrape_dynamic_data

#Tampilan Data Seluruh Barang
class IndexView(generic.ListView):
    template_name = "motorterbangApp/barang/daftar-barang.html"
    context_object_name = "daftar_barang"

    def get_queryset(self):
        return Barang.objects.order_by("no_katalog")[:30]

#Tambilan Detail Barang
class DetailView(generic.DetailView):
    model = Barang
    template_name = "motorterbangApp/barang/detail-barang.html"

#Tampilan Tambah Barang
def tambahBarang(request):
    form = BarangForm
    if request.method == 'POST':
        form = BarangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('motorterbangApp:daftar_barang')
    else:
        context = {'form':form}
    return render(request, 'motorterbangApp/barang/tambah-barang.html', context)

#Tampilan Edit Barang
def editBarang(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    if request.method == 'POST':
        form = BarangForm(request.POST, instance=barang)
        if form.is_valid():
            form.save()
            return redirect('motorterbangApp:detail_barang', pk=barang.id)
    else:
        form = BarangForm(instance=barang)
    return render(request, 'motorterbangApp/barang/edit-barang.html', {'form': form, 'item': barang})

def index(request):
    return render(request, "motorterbangApp/index.html")


#Web Scraper
def dynamic_scrape_view(request):
    """
    Django view to scrape data dynamically using Playwright.
    """
    url = request.GET.get('url', 'https://sipt.pom.go.id/laporan/pengawasan/main')  # Allow dynamic URL input
    try:
        data = scrape_dynamic_data(url)
        return JsonResponse({"success": True, "data": data})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})