# Generated by Django 3.0.6 on 2020-05-23 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Password',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
    ]
