# Generated by Django 2.1 on 2018-08-11 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roboapp', '0021_auto_20180811_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='author',
        ),
    ]