# Generated by Django 2.2.24 on 2022-01-18 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_payholder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payholder',
            old_name='true',
            new_name='confirm',
        ),
        migrations.RemoveField(
            model_name='payholder',
            name='cardNumber',
        ),
        migrations.AddField(
            model_name='payholder',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Card'),
        ),
    ]
