# Generated by Django 4.2.1 on 2023-07-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanIFYWOD', '0026_alter_eventworkout_workout_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventworkout',
            name='workout_demo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]