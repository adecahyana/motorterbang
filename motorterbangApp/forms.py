from django.forms import ModelForm, Textarea, TextInput, CheckboxInput, Select
from .models import Barang

#Form untuk Tambah Barang
class BarangForm(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        widgets = {
            "jenis_barang": Select(attrs={"class": "mt-1 mb-3 bg-gray-100 text-gray-700 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-gray-600"}),
            "nama_barang": TextInput(attrs={"class": "mt-1 mb-3 bg-gray-100 text-gray-700 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-gray-600"}),
            "no_katalog": TextInput(attrs={"class": "mt-1 mb-3 bg-gray-100 text-gray-700 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-gray-600"}),
            "spesifikasi": Textarea(attrs={"class": "mt-1 mb-3 bg-gray-100 text-gray-700 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-gray-600"}),
            "stok": TextInput(attrs={"class": "mt-1 mb-3 bg-gray-100 text-gray-700 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-gray-600"}),
            "pdn": CheckboxInput(attrs={"class": "mt-1 mb-1 bg-gray-100 text-gray-700 p-3  focus:outline-none focus:ring-2 focus:ring-gray-600"}),
        }

