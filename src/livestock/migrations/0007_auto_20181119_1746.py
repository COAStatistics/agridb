# Generated by Django 2.0.9 on 2018-11-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0006_livestock_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestock',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
