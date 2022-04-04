# Generated by Django 4.0.3 on 2022-04-02 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeleBot', '0005_exchangedata_yen_rate_exchangedata_yuan_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreviousMessages',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='TeleBot.telebotusers')),
                ('previous_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeleBot.exchangedata')),
            ],
        ),
    ]
