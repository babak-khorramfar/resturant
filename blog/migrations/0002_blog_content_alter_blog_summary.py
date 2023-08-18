# Generated by Django 4.2.4 on 2023-08-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, max_length=4000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.TextField(max_length=150),
        ),
    ]
