# Generated by Django 3.0.7 on 2020-06-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Noticeboard',
            new_name='Notice',
        ),
        migrations.RenameModel(
            old_name='Teachers',
            new_name='Teacher',
        ),
    ]