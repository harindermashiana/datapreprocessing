# Generated by Django 2.0.2 on 2018-05-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaner', '0002_auto_20180505_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_field',
            field=models.FileField(upload_to=''),
        ),
    ]
