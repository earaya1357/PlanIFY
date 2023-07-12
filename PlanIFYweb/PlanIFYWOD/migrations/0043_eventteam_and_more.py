# Generated by Django 4.2.1 on 2023-07-12 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlanIFYWOD', '0042_event_event_city_event_event_zip'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlanIFYWOD.event')),
            ],
        ),
        migrations.RenameField(
            model_name='eventparticipant',
            old_name='event_joing_date',
            new_name='event_join_date',
        ),
        migrations.RenameField(
            model_name='eventparticipant',
            old_name='event_id_number',
            new_name='event_name',
        ),
        migrations.RenameField(
            model_name='eventparticipant',
            old_name='participants',
            new_name='participant',
        ),
        migrations.RemoveField(
            model_name='eventparticipant',
            name='email_of_athlete',
        ),
        migrations.RemoveField(
            model_name='eventparticipant',
            name='first_name_of_athlete',
        ),
        migrations.RemoveField(
            model_name='eventparticipant',
            name='last_name_of_athlete',
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='address_of_participant',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='age_of_participant',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='city_of_participant',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='email_of_participant',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='first_name_of_participant',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='gender_of_participant',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='last_name_of_participant',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='role',
            field=models.CharField(choices=[('Athlete', 'Athlete'), ('Judge', 'Judge'), ('General', 'General')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='state_of_participant',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='zip_code_of_participant',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PlanIFYWOD.useraccount'),
        ),
        migrations.AlterField(
            model_name='eventprizes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='EventHelp',
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PlanIFYWOD.eventteam'),
        ),
    ]
