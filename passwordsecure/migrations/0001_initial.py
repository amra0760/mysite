# Generated by Django 2.0.5 on 2018-05-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
                ('site_name', models.CharField(max_length=1000)),
            ],
        ),
    ]