# Generated by Django 4.0.4 on 2022-05-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud', '0008_classe_room_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='price',
        ),
        migrations.AddField(
            model_name='classe',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
