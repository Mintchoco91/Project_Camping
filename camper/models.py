from django.db import models

class Product(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50)  # Field name made lowercase.
    category = models.CharField(db_column='CATEGORY', max_length=30)  # Field name made lowercase.
    thumbnail_img = models.CharField(db_column='THUMBNAIL_IMG', max_length=500, blank=True, null=True)  # Field name made lowercase.
    detail_img = models.CharField(db_column='DETAIL_IMG', max_length=500, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='UPDATED_AT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCT'