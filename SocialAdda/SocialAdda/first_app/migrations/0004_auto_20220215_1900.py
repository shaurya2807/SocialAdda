# Generated by Django 3.2.5 on 2022-02-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_conf_visible'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conf',
            options={'ordering': ['visibleTime']},
        ),
        migrations.AddField(
            model_name='conf',
            name='visibleTime',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='conf',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
