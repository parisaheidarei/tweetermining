# Generated by Django 3.2.4 on 2021-06-24 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0003_baseusers_screen_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseusers',
            name='screen_name',
        ),
    ]
