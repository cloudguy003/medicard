# Generated by Django 3.1.3 on 2020-12-03 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_acc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='uploaded_at',
            new_name='created_at',
        ),
    ]
