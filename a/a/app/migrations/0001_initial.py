# Generated by Django 2.2.24 on 2022-01-12 13:11

import creditcards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', creditcards.models.CardNumberField(max_length=25)),
                ('card_exp', creditcards.models.CardExpiryField()),
                ('card_sec', creditcards.models.SecurityCodeField(max_length=4)),
                ('name_on_card', models.CharField(max_length=40)),
                ('holder_id_check', models.IntegerField(blank=True)),
                ('facement', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Holder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unq_id', models.IntegerField()),
                ('activated', models.CharField(default='None', max_length=9)),
                ('card', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Card')),
            ],
        ),
    ]
