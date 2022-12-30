from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class ContactUs(models.Model):

    Name = models.CharField(max_length=60)
    Subject =  models.CharField(max_length=60)
    Email = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Chat =  models.CharField(max_length=6000)
    def __str__(self):
        return self.Name +" "+ str(self.id)
    


class Home_Slider(models.Model):

    Name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='home/sliders')
    Link =models.CharField(max_length=600)
    def __str__(self):
        return self.Name

class Block_Buster_Deal(models.Model):
    Item = models.ForeignKey(Product,on_delete=models.CASCADE)


    