# Generated by Django 4.0.5 on 2022-07-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_students', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('name_of_book', models.CharField(max_length=100)),
            ],
        ),
    ]
