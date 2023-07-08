# Generated by Django 4.2.1 on 2023-07-08 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlanIFYWOD', '0032_eventhelp'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_state',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_tshirts_price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.CreateModel(
            name='EventPrizes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('position', models.CharField(max_length=30)),
                ('prize_amount', models.FloatField(default=0.0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlanIFYWOD.event')),
            ],
        ),
    ]
