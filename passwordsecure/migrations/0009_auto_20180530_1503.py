# Generated by Django 2.0.5 on 2018-05-30 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwordsecure', '0008_auto_20180530_1503'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Email',
        ),
    ]
