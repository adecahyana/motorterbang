from django.db import models
import uuid


#Jenis Barang
class Jenis(models.Model):
    nama_jenis = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_jenis



#Nama Laboratorium
class Laboratorium(models.Model):
    nama_laboratorium = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_laboratorium


#Barang
class Barang(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jenis_barang = models.ForeignKey(Jenis, on_delete=models.CASCADE, default=1)
    nama_barang = models.CharField(max_length=200)
    no_katalog = models.CharField(max_length=50)
    spesifikasi = models.TextField()
    stok = models.PositiveIntegerField(default=0)
    pdn = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_barang
    
#Sumber Anggaran
class SumberAnggaran(models.Model):
    jenis_sumber = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.jenis_sumber
    
#Mata Anggaran Kegiatan
class MataAnggaran(models.Model):
    tahun_anggaran = models.PositiveIntegerField()
    kode_akun = models.CharField(max_length=100)
    nama_kegiatan = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_kegiatan
    
#Komponen MAK
class Komponen(models.Model):
    mata_anggaran = models.ForeignKey(MataAnggaran, on_delete=models.CASCADE, default=1)
    sumber_anggaran = models.ForeignKey(SumberAnggaran, on_delete=models.CASCADE, default=1)
    kode_belanja = models.CharField(max_length=50)
    nama_komponen = models.CharField(max_length=250)
    jumlah_anggaran = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_komponen

#Penyedia
class Penyedia(models.Model):
    nama_penyedia = models.CharField(max_length=100)
    alamat_penyedia = models.CharField(max_length=300)
    pimpinan_penyedia = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_penyedia

#Referensi Harga
class ReferensiHarga(models.Model):
    nama_barang = models.ForeignKey(Barang, on_delete=models.CASCADE, default=1)
    referensi_penyedia = models.CharField(max_length=100)
    harga_referensi = models.PositiveIntegerField(default=0)
    link_referensi = models.CharField(max_length=300)
    data_referensi = models.FileField()