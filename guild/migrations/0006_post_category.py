# Generated by Django 2.1.7 on 2019-03-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0005_auto_20190328_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='None', max_length=50),
        ),
    ]