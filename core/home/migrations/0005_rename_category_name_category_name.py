# Generated by Django 4.2.1 on 2023-05-31 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_name_category_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]