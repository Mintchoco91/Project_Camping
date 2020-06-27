from django.db import models

# Create your models here.
class Account(models.Model):
    ID = models.CharField(max_length = 200)
    password = models.CharField(max_length = 500)
    created_at = models.DataTimeField(auto_now_add = True)
    updated_at = models.DataTimeField(auto_now = True)