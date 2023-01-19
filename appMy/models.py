from django.db import models

# Create your models here.

class Card(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik"), max_length=500)
    date_now = models.DateTimeField(("Tarih Saat"), auto_now_add=False)
    
    def __str__(self):
        return self.title
