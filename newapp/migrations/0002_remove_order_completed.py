# Generated by Django 3.2.2 on 2021-06-19 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='completed',
        ),
    ]
