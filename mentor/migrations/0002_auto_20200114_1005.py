# Generated by Django 2.2 on 2020-01-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorprofile',
            name='description',
            field=models.CharField(default='This is a default text', max_length=500),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='slug',
            field=models.SlugField(default='default-slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
