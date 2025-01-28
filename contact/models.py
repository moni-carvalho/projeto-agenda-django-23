from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key) - - automático
# Create your models here.
# first_name (string), last_name (string), phone (string)
# email (email), create_date (date), descriptin (text)
#depois
# category (foreign key), show (boolean),picture (imagem) 
# Depois
# owner (foreign key),
# picture (imagem)

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank= True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank= True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m/')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    


    
    

