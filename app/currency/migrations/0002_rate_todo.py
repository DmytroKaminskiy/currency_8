# Generated by Django 4.0.6 on 2022-07-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='todo',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
