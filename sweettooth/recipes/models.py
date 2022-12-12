from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Label(models.Model):
   name = models.CharField(max_length=50,null = False,blank =False)
   


   def __str__(self):
        return self.name

class Recipe(models.Model):

    name = models.CharField(max_length=50 , blank = False , null = False)
    label = models.ForeignKey(Label,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    serving = models.IntegerField(blank = True,null = True)
    description  =models.TextField(max_length = 300,blank = True , null = True)  
    ingredient =models.TextField(blank = True,null = True)  
    method = models.TextField(blank = False , null = False)
    image = models.ImageField(upload_to = 'upload/',blank = True , null = True)
   



    def __str__(self):
        return self.name
    
    def snippet(self):
        return self.description[:50]+'...'
