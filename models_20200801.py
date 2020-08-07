# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Member(models.Model):
    mno = models.AutoField(db_column='MNO', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=20)  # Field name made lowercase.
    user_pw = models.CharField(db_column='USER_PW', max_length=20)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=10)  # Field name made lowercase.
    enrolldate = models.DateTimeField(db_column='ENROLLDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEMBER'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CamperPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'camper_post'
