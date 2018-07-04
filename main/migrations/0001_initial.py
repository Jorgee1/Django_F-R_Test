# Generated by Django 2.0.7 on 2018-07-04 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Languaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.CharField(default='', max_length=10, unique=True)),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=200, unique=True)),
                ('favorite_food', models.CharField(default='', max_length=400)),
                ('city', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.City')),
                ('color', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Color')),
                ('languaje', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Languaje')),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
    ]