# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pet(models.Model):
    objects = models.Manager()
    SEX_CHOICES = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30,blank=True)
    descriptions = models.TextField()
    sex = models.CharField(choices= SEX_CHOICES, max_length = 1,blank = True )
    submission_Date = models.DateTimeField(null=False, blank=False,
                   verbose_name=u'Fecha de creación',auto_now_add=True)
    age = models.IntegerField(null = True)
    vaccinations = models.ManyToManyField('Vaccine', blank = True)

class Vaccine(models.Model):
    objects = models.Manager()
    name = models.TextField(max_length=50)

    
