from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    link = models.URLField(max_length=200)
    description = models.TextField(max_length=300)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    @classmethod
    def filter_by_category(cls,category):
        images = Images.objects.filter(category=category)
        return images
    
    def __str__(self):
        return self.name