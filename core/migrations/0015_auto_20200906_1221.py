# Generated by Django 3.1.1 on 2020-09-06 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200906_1204'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='director',
            unique_together={('first_name', 'last_name')},
        ),
    ]