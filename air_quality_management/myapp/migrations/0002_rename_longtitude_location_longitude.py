# Generated by Django 3.2.20 on 2023-09-08 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='longtitude',
            new_name='longitude',
        ),
    ]