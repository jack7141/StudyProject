# Generated by Django 4.0.4 on 2022-05-10 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='writer',
        ),
    ]