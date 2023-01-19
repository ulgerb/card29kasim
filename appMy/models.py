from django.db import models

# Create your models here.

class Card(models.Model):
    brand = models.CharField(("Marka"), max_length=50, null=True)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik"), max_length=500)
    date_now = models.DateTimeField(("Tarih Saat"), auto_now_add=False)
    price = models.IntegerField(("Fiyat"), null=True)
    image = models.FileField(("Ürün Resmi"), upload_to='', max_length=100, blank=True)
    
    def __str__(self):
        return self.title
