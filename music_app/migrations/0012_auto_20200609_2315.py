# Generated by Django 2.2 on 2020-06-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0011_auto_20200609_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='dedicated_by',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='dedicated_for',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
