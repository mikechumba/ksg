# Generated by Django 2.1.7 on 2019-03-28 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0010_auto_20190328_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='genre',
        ),
    ]