# Generated by Django 3.2.4 on 2021-07-12 08:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0004_remove_baseusers_screen_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='allusers',
            name='checked',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
