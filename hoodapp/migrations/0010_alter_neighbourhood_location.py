# Generated by Django 4.0.5 on 2022-06-21 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0009_business_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.location'),
        ),
    ]