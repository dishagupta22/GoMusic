# Generated by Django 2.2 on 2020-06-08 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0010_auto_20200608_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='song_album', to='music_app.album'),
        ),
    ]