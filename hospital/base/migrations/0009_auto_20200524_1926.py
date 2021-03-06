# Generated by Django 3.0.6 on 2020-05-24 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200524_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(limit_choices_to={'Registeras': 'Doctor'}, on_delete=django.db.models.deletion.CASCADE, to='base.Profile'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(limit_choices_to={'Registeras': 'Patient'}, on_delete=django.db.models.deletion.CASCADE, to='base.Profile'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], default=None, max_length=20)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Doctor')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Patient')),
            ],
        ),
    ]
