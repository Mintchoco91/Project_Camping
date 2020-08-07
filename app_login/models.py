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