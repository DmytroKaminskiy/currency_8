# Generated by Django 4.1 on 2022-08-22 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_source_remove_rate_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='currency.source'),
        ),
    ]