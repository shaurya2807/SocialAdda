# Generated by Django 3.2.5 on 2022-02-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20220213_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conf',
            name='visible',
            field=models.BooleanField(),
        ),
    ]
