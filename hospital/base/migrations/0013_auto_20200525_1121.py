# Generated by Django 3.0.6 on 2020-05-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20200525_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Registeras',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], default='jeet', max_length=30),
        ),
    ]
