# Generated by Django 3.0.6 on 2020-05-24 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20200524_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Address',
            field=models.CharField(default='Address', max_length=500),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='BloodType',
            field=models.CharField(default='BloodType', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Name',
            field=models.CharField(default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.Profile'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Address',
            field=models.CharField(default='Address', max_length=500),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='BloodType',
            field=models.CharField(default='BloodType', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.Profile'),
        ),
    ]
