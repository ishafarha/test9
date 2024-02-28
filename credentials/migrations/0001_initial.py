# Generated by Django 4.2.6 on 2024-02-23 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
                ('actors', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('link', models.URLField()),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
