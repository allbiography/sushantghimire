from django.db import models
from django.contrib.auth.models import User


class personal_info(models.Model):
    student_name = models.OneToOneField(User, null=True, on_delete=models.DO_NOTHING)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to='images/')
    faculty = models.CharField(max_length=222)
    grade = models.IntegerField()
    section = models.CharField(max_length=222)
    first_ordered_book = models.CharField(max_length=20, blank=True, null=True)
    second_ordered_book = models.CharField(max_length=20, blank=True, null=True)

    # def __str__(self):
    #     return f'{self.user}'


class Book_Order(models.Model):
    fk = models.ForeignKey(personal_info, on_delete=models.CASCADE, null=True, blank=True)
    name_of_book = models.CharField(max_length=111)

    # to link the personal_info with Book_Order
    @property
    def name(self):
        return self.fk.name


class Text_Book(models.Model):
    name = models.CharField(max_length=222)
    writer = models.CharField(max_length=22, null=True)
    description = models.TextField(max_length=2222)
    price = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=8888)
    book_pic = models.ImageField(upload_to='books/', null=True, blank=True)
    student = models.CharField(max_length=100, blank=True)
    teacher = models.CharField(max_length=100, blank=True)
    Issued_date = models.DateTimeField(null=True, blank=True)
    Returned_date = models.DateTimeField(null=True, blank=True)


class Programming_Book(models.Model):
    name = models.CharField(max_length=222)
    writer = models.CharField(max_length=22)
    description = models.TextField(max_length=2222)
    price = models.FloatField(null=True)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=8888)
    student = models.CharField(max_length=100, blank=True)
    teacher = models.CharField(max_length=100, blank=True)


class Novel(models.Model):
    name = models.CharField(max_length=222)
    writer = models.CharField(max_length=22)
    description = models.TextField(max_length=2222)
    price = models.FloatField(null=True)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=8888)
    student = models.CharField(max_length=100, blank=True)
    teacher = models.CharField(max_length=100, blank=True)




