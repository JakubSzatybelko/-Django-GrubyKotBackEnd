# Generated by Django 3.2.9 on 2021-11-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_apointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apointment',
            name='type',
            field=models.CharField(choices=[('Konsultacja', 'Consultation'), ('Sesja', 'Tattooing'), ('Poprawki', 'Touchup')], max_length=255),
        ),
    ]
