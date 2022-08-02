from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public = True)

    def search(self, query, user = None):
        lookup = models.Q(title__icontains = query) | models.Q(content__icontains = query)
        qs = self.is_public().filter(models.Q(title__icontains = query) | models.Q(content__icontains = query))
        if user is not None:
            qs = qs.filter(user = user)
        
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, username):
        return self.get_queryset().search(query, user = username)
    # def search(self, query, user=None):
    #     # title__icontains or content__icontains:  
    #     # It's a case-insensitive containment test.
    #     return Product.objects.filter(public = True).filter(models.Q(title__icontains = query) | models.Q(content__icontains = query))
    

class Product(models.Model):
    user = models.ForeignKey(User, default = 1, null = True ,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField(blank = True, null = True) # Description of the product
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    objects = ProductManager()

    def discounted_price(self):
        res = self.price // 20
        return self.price - res

    def __str__(self):
        return self.title