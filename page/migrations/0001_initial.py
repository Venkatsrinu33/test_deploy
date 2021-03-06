# Generated by Django 3.0.2 on 2020-01-03 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=225)),
                ('phoneno', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=8)),
                ('createddate', models.DateField(auto_now=True)),
            ],
        ),
    ]
