# Generated by Django 3.2.6 on 2021-08-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0003_rename_livelurl_project_liveurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(max_length=150),
        ),
    ]
