# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Blindbook(models.Model):
    bookno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    publisher = models.CharField(max_length=1000, blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BLINDBOOK'

    def __str__(self):
        return self.title


class City(models.Model):
    sido_nm = models.CharField(primary_key=True, max_length=10)
    gungu_nm = models.CharField(max_length=10)
    libnumber = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CITY'
        unique_together = (('sido_nm', 'gungu_nm'),)

    def __str__(self):
        return self.sido_nm + ' ' + self.gungu_nm


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    sido_nm = models.CharField(max_length=10, blank=True, null=True)
    gungu_nm = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USER'

    def __str__(self):
        return self.id


class Library(models.Model):
    libno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    sido_nm = models.CharField(max_length=10, blank=True, null=True)
    gungu_nm = models.CharField(max_length=10, blank=True, null=True)
    close_day = models.CharField(max_length=1000, blank=True, null=True)
    every_open = models.CharField(max_length=10, blank=True, null=True)
    every_close = models.CharField(max_length=10, blank=True, null=True)
    sat_open = models.CharField(max_length=10, blank=True, null=True)
    sat_close = models.CharField(max_length=10, blank=True, null=True)
    holiday_open = models.CharField(max_length=10, blank=True, null=True)
    holiday_close = models.CharField(max_length=10, blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    books = models.IntegerField(blank=True, null=True)
    loanable_books = models.IntegerField(blank=True, null=True)
    loanable_days = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    site = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library'

    def __str__(self):
        return self.name