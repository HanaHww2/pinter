# Generated by Django 3.1.5 on 2021-01-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]