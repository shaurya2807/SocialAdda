# Generated by Django 3.2.5 on 2022-02-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conf',
            name='visible',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='conf',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]