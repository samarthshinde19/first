# Generated by Django 4.0.4 on 2022-07-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_requesting_cord_requesting_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesting',
            name='users',
            field=models.CharField(default='-', max_length=20),
        ),
    ]
