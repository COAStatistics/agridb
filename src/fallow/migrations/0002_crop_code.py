# Generated by Django 2.0.9 on 2018-11-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='code',
            field=models.CharField(default='default', max_length=50, unique=True, verbose_name='Code'),
        ),
    ]
