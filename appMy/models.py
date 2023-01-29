from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    date_now = models.DateField(("Tarih"), auto_now_add=True)
    
    def __str__(self):
        return self.title

class Card(models.Model):
    brand = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik"), max_length=500)
    date_now = models.DateTimeField(("Tarih Saat"), auto_now_add=False)
    price = models.IntegerField(("Fiyat"), null=True)
    image = models.FileField(("Ürün Resmi"), upload_to='', max_length=100, blank=True)
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    card = models.ForeignKey(Card, verbose_name=("Card"), on_delete=models.CASCADE)
    name = models.CharField(("Yorumcu"), max_length=50)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"),max_length=500)
    date_now = models.DateTimeField(("Yorum Yapılma Zamanı"), auto_now_add=True)
    
    def __str__(self):
        return self.card
