# Generated by Django 4.0.4 on 2022-07-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requesting',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('declined', 'declined')], default='pending', max_length=25),
        ),
    ]
