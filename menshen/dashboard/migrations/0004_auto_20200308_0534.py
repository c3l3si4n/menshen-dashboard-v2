# Generated by Django 3.0.4 on 2020-03-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_vulnerability_date_found'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerability',
            name='target',
        ),
        migrations.DeleteModel(
            name='Target',
        ),
        migrations.DeleteModel(
            name='Vulnerability',
        ),
    ]
