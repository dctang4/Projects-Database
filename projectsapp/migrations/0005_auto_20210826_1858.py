# Generated by Django 3.2.6 on 2021-08-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0004_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='giturl',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='project',
            name='liveurl',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='project',
            name='project',
            field=models.CharField(max_length=50),
        ),
    ]
