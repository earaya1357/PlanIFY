# Generated by Django 4.2.1 on 2023-07-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanIFYWOD', '0029_remove_event_event_start_time_alter_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_registration_date_close',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_registration_date_open',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]