# Generated by Django 2.1.7 on 2019-03-28 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0009_auto_20190328_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guild.Role'),
        ),
    ]
