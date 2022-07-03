# Generated by Django 4.0.4 on 2022-07-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_data_x'),
    ]

    operations = [
        migrations.CreateModel(
            name='cont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('message', models.TextField()),
                ('date', models.CharField(default='-', max_length=20)),
                ('time', models.CharField(default='-', max_length=20)),
            ],
        ),
    ]
