# Generated by Django 4.0.3 on 2022-03-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_email_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_confirmed',
            new_name='email_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]