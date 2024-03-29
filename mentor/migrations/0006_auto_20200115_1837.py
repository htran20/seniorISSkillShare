# Generated by Django 2.2 on 2020-01-15 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0005_mentorprofile_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentorprofile',
            name='education',
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='school',
            field=models.CharField(default='Default school', max_length=100),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='school_end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='school_start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
