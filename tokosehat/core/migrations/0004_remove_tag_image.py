# Generated by Django 2.2.3 on 2019-08-30 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190830_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='image',
        ),
    ]