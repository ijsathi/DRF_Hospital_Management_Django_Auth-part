# Generated by Django 5.0.6 on 2024-07-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='service/images/'),
        ),
    ]
