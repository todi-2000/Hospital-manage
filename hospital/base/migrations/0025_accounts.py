# Generated by Django 3.0.6 on 2020-06-06 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_auto_20200605_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('paid', models.IntegerField(default=0)),
                ('outstanding', models.IntegerField(default=0)),
                ('invoice', models.ImageField(upload_to='patient_invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Patient')),
            ],
        ),
    ]