# Generated by Django 3.2.5 on 2022-05-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('account_alias', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
        ),
    ]
