# Generated by Django 4.2.1 on 2023-07-11 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlanIFYWOD', '0040_alter_useraccount_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_tshirt_image',
            field=models.ImageField(blank=True, null=True, upload_to='shirt-images'),
        ),
    ]