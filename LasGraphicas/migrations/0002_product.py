# Generated by Django 5.1.6 on 2025-03-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LasGraphicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
