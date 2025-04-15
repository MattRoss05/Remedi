# Generated by Django 5.1.7 on 2025-03-26 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('patient', 'Patient'), ('provider', 'Provider')], default='provider', max_length=10),
        ),
    ]
