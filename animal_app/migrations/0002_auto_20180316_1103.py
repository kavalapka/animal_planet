# Generated by Django 2.0.3 on 2018-03-16 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='animal_name',
            new_name='name',
        ),
    ]