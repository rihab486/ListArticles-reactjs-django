from django.db import models
from django.db.models.deletion import SET_DEFAULT

import datetime

class Article (models.Model):
    declarationarabe = models.FloatField(blank=True,null=True)
    declarationlatine = models.FloatField(blank=True,null=True)
    classe = models.CharField(max_length=200 ,  blank=True, null=True) 
    unite=models.CharField(max_length=200 ,  blank=True, null=True) 
    validité=models.DateField(default=datetime.datetime.now(), blank=True,null=True) 
    numero_de_lot=models.IntegerField(blank=True,null=True) 
    remarque=models.CharField(max_length=200 ,  blank=True, null=True) 
    variable =models.BooleanField(default=False) 
    ch =models.BooleanField(default=False)
    idClassification = models.ForeignKey('article.Classification', blank=True, null=True,   on_delete=SET_DEFAULT,  default=None ) 

class Classification (models.Model):
    nom =models.CharField(max_length=200 ,  blank=True, null=True) 
