# Generated by Django 3.2.8 on 2021-11-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='mticket',
            field=models.CharField(default='', max_length=100, null=True, unique=True, verbose_name='movie ticket'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='mimg',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='movie image'),
        ),
    ]
