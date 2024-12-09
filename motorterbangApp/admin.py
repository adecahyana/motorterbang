from django.contrib import admin
from .models import Barang, Jenis, Laboratorium, MataAnggaran, Komponen

# Register your models here.
admin.site.register([Barang, Jenis, Laboratorium, MataAnggaran, Komponen])