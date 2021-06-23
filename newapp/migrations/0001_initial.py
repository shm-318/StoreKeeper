# Generated by Django 3.2.2 on 2021-06-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('quantity', models.CharField(blank=True, max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
