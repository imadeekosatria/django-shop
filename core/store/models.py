from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Product(models.Model):
    nama = models.CharField(max_length=200, unique=True)
    gambar = models.ImageField(default=None, upload_to='products', blank=True, null=True)
    deskripsi = models.CharField(max_length=500, blank=True)
    harga = models.IntegerField(default=None, blank=True)
    slug = models.SlugField(default="", null=False, blank=True, unique=True)
    visitor_product = models.IntegerField(default=0)
    key_words = models.CharField(max_length=100, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nama)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        return super().save(*args, **kwargs)

class Halaman(models.Model):
    logo = models.ImageField(default=None, upload_to='profile', blank=True, null=True)
    nama_web = models.CharField(max_length=100, default='Store', unique=True)
    tentang_toko = models.TextField(max_length=500, default=None, null=True)
    email = models.EmailField(max_length=100, default=None, null=True)
    country = models.CharField(max_length=100, default=None, blank=True, null=True)
    city = models.CharField(max_length=100, default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    phone = models.CharField(default=None, max_length=20, blank=True, null=True)
    zip = models.IntegerField(default=None, blank=True, null=True)
    instagram = models.URLField(default=None, blank=True, null=True)
    facebook = models.URLField(default=None, blank=True, null=True)
    wa_message = models.CharField(max_length=500, default=None, blank=True, null=True)
    key_words_page = models.CharField(max_length=100, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nama_web)
    
class Contact(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name='Date')
    count = models.IntegerField(default=None)

    def __str__(self):
        return str(self.created_at)

class Visitor(models.Model):
    count = models.IntegerField(default=None)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at.strftime("%Y-%m-%d"))