# Generated by Django 3.2.4 on 2021-06-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='date',
            field=models.DateField(editable=False, verbose_name='Date'),
        ),
    ]
