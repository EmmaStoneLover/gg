# Generated by Django 3.1.2 on 2020-11-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=120)),
                ('text', models.CharField(max_length=120)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
