# Generated by Django 3.0.7 on 2020-06-28 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_event_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AddField(
            model_name='picture',
            name='event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.Event'),
            preserve_default=False,
        ),
    ]