# Generated by Django 4.1.7 on 2023-03-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_app', '0002_remove_message_status_message_is_sent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_sent',
        ),
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[(False, 'Not sent'), (True, 'Sent')], default=False, max_length=3, verbose_name='Статус отправки'),
        ),
    ]
