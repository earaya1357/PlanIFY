# Generated by Django 4.2.1 on 2023-07-13 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanIFYWOD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipant',
            name='event_join_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
