# Generated by Django 4.1.4 on 2022-12-18 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comenapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coments',
            name='algo',
        ),
    ]