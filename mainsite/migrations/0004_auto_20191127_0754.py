# Generated by Django 2.2.7 on 2019-11-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_events_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendee',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='atendee',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=20, null=True),
        ),
    ]
