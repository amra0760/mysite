# Generated by Django 2.0.5 on 2018-05-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordsecure', '0005_auto_20180530_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='email',
            field=models.CharField(max_length=1000),
        ),
    ]