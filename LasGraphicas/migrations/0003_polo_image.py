# Generated by Django 5.1.6 on 2025-03-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LasGraphicas', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='polo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
