# Generated by Django 4.0.3 on 2022-03-19 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dollar_rate', models.FloatField(help_text='Dollar exchange rate', max_length=4)),
                ('euro_rate', models.FloatField(help_text='Euro exchange rate', max_length=1000)),
                ('time_rate', models.DateTimeField(help_text='time when rate was obtained')),
            ],
        ),
    ]