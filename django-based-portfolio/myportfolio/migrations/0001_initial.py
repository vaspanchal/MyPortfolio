# Generated by Django 5.0.6 on 2024-07-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('libraries', models.CharField(max_length=100)),
                ('database', models.CharField(max_length=100)),
                ('ml', models.CharField(max_length=100)),
            ],
        ),
    ]
