# Generated by Django 4.2.10 on 2024-02-28 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.IntegerField(default='456def'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.TextField(default='123abc'),
            preserve_default=False,
        ),
    ]
