# Generated by Django 3.2.9 on 2022-10-04 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20221004_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainadmin',
            name='group_home',
        ),
        migrations.AddField(
            model_name='mainadmin',
            name='group_home',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.grouphome'),
        ),
    ]
