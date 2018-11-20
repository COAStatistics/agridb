# Generated by Django 2.0.9 on 2018-11-20 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0008_auto_20181115_1141'),
        ('fallow', '0003_declare_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='fallowtransfer',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='household.Year', verbose_name='Year'),
        ),
    ]
