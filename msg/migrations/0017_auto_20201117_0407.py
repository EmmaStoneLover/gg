# Generated by Django 3.1.2 on 2020-11-17 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0016_auto_20201117_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='card_clr',
            field=models.CharField(default='text-white', max_length=100, null=True, verbose_name='Текст'),
        ),
    ]
