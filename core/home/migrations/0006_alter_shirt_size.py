# Generated by Django 4.2.1 on 2023-05-31 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_category_name_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='size',
            field=models.CharField(max_length=10),
        ),
    ]