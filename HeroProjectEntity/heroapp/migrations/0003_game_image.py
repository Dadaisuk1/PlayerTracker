# Generated by Django 5.1.2 on 2024-11-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroapp', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
