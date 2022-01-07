from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone

class urlModel(models.Model):
    picurl = models.CharField(max_length = 5000, null = True, blank = True)
    
    def __str__(self):
        return str(self.id) +"-> " + str(self.picurl)

class blogMOdel(models.Model):
    title = models.CharField(max_length = 5000, null = True, blank = True)
    content = models.CharField(max_length = 500000, null = True, blank = True)
    
    def __str__(self):
        return str(self.title)

class contactModel(models.Model):
    name = models.CharField(max_length = 5000, null = True, blank = True)
    phonenumber = models.CharField(max_length = 5000, null = True, blank = True)
    email = models.CharField(max_length = 5000, null = True, blank = True)
    message = models.CharField(max_length = 50000, null = True, blank = True)
    
    def __str__(self):
        return str(self.name)
