# Generated by Django 4.0.5 on 2022-07-12 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('History', '0002_remove_history_content_type_history_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='user',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='history',
            name='object_id',
        ),
    ]