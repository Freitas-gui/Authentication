# Generated by Django 3.0.5 on 2020-04-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileperson',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]