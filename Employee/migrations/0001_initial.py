# Generated by Django 4.1.3 on 2022-11-23 06:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('firstName', models.TextField(max_length=100)),
                ('lastName', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('address', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
                ('position', models.TextField(max_length=100)),
                ('background', models.CharField(max_length=500)),
            ],
        ),
    ]
