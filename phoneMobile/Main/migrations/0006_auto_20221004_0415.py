# Generated by Django 3.2.9 on 2022-10-04 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_alter_mainadmin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainadmin',
            name='group_home',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Main.grouphome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainadmin',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
