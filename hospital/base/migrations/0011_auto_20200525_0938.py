# Generated by Django 3.0.6 on 2020-05-25 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0010_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Outstanding',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='Paid',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
