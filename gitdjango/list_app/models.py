from django.db import models


class list_app(models.Model):

    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    vid = models.CharField(max_length=200)
    population = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')
    name_1 = models.CharField(max_length=200)
    price_1 = models.IntegerField(default=0)  
    image_1 = models.ImageField(upload_to='images')
    name_2 = models.CharField(max_length=200)
    price_2 = models.IntegerField(default=0)  
    image_2 = models.ImageField(upload_to='images')
    name_3 = models.CharField(max_length=200)
    price_3 = models.IntegerField(default=0)  
    image_3 = models.ImageField(upload_to='images')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '無料ゲームリスト'

# Create your models here.
