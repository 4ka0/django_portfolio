# Generated by Django 3.0.2 on 2020-01-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200120_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
