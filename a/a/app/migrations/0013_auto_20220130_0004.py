# Generated by Django 2.2.24 on 2022-01-29 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_cardholder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='facement',
        ),
        migrations.RemoveField(
            model_name='card',
            name='holder_id_check',
        ),
    ]
