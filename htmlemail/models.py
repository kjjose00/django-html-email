from django.db import models
from django.http import HttpResponse
from django.shortcuts import render

# Create your models here.

class HTMLEMAIL(models.Model):
    html_email=models.FileField(upload_to='documents/')

