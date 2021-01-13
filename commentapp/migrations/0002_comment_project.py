# Generated by Django 3.1.5 on 2021-01-13 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_auto_20210113_2045'),
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='projectapp.project'),
        ),
    ]
