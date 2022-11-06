# Generated by Django 4.0.3 on 2022-04-04 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeleBot', '0008_userpreviousmessages_time_dollar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='TeleBot.telebotusers')),
                ('feedback', models.TextField(help_text="User's feedback")),
            ],
        ),
    ]