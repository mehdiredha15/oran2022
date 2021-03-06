# Generated by Django 4.0.4 on 2022-05-27 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stud', '0005_room_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nb_tickets', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='Session',
            field=models.CharField(default=0.0026706231454005935, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='stade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stud.stade'),
        ),
    ]
