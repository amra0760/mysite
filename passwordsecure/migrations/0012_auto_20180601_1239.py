# Generated by Django 2.0.5 on 2018-06-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordsecure', '0011_remove_email_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='website',
        ),
        migrations.AddField(
            model_name='website',
            name='email',
            field=models.CharField(default='johndoe@example.com', max_length=1000),
        ),
        migrations.AddField(
            model_name='website',
            name='password',
            field=models.CharField(default='password123', max_length=1000),
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
