# Generated by Django 2.2.24 on 2022-01-17 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holder',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Card'),
        ),
    ]