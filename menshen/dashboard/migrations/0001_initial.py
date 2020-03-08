# Generated by Django 3.0.4 on 2020-03-08 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve', models.CharField(max_length=255)),
                ('priority', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Target')),
            ],
        ),
    ]
