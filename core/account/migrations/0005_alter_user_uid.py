# Generated by Django 4.2.1 on 2023-06-03 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_u_id_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
