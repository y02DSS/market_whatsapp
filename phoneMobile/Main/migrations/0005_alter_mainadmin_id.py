# Generated by Django 3.2.9 on 2022-10-04 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_grouphome_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainadmin',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]