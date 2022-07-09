from django.contrib import admin
from .models import Text_Book, Programming_Book,  Book_Order, Novel
from .models import personal_info


@admin.register(personal_info)
class personal_infoAdmin(admin.ModelAdmin):
    list_display = (
        'student_name', 'profile_picture', 'first_ordered_book',
        'second_ordered_book',)
    ordering = ('student_name',)
    search_fields = ('profile_picture',)


@admin.register(Book_Order)
class Book_OrderAdmin(admin.ModelAdmin):
    list_display = ('fk', 'name_of_book',)
    ordering = ('fk',)
    search_fields = ('fk', 'name_of_book',)


@admin.register(Text_Book)
class Text_BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'teacher', 'book_pic', 'Issued_date', 'Returned_date')
    ordering = ('name',)
    search_fields = ('name', 'writer', 'price', 'stock', 'teacher',)


@admin.register(Programming_Book)
class Programming_BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'teacher',)
    ordering = ('name',)
    search_fields = ('name', 'writer', 'price', 'stock', 'student', 'teacher',)


@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'teacher',)
    ordering = ('name',)
    search_fields = ('name', 'writer', 'price', 'stock', 'student', 'teacher',)


