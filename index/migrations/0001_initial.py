# Generated by Django 3.2.8 on 2021-11-02 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradetype', models.CharField(max_length=100, unique=True, verbose_name='grade type')),
                ('isDelete', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=100, unique=True, verbose_name='movie name')),
                ('mduration', models.IntegerField()),
                ('mimg', models.ImageField(upload_to='images/')),
                ('isDelete', models.BooleanField(default=True)),
                ('mgradetype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.grade')),
            ],
        ),
    ]
