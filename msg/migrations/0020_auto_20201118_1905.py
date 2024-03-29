# Generated by Django 3.1.2 on 2020-11-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0019_auto_20201118_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='card_bg_color_choice',
            field=models.CharField(choices=[('bg-dark', 'bg-dark'), ('bg-light', 'bg-light'), ('bg-primary', 'bg-primary'), ('bg-secondary', 'bg-secondary'), ('bg-success', 'bg-success'), ('bg-danger', 'bg-danger'), ('bg-warning', 'bg-warning'), ('bg-info', 'bg-info')], default='bg-dark', max_length=100, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='message',
            name='card_font_color_choice',
            field=models.CharField(choices=[('text-white', 'text-white'), ('text-dark', 'text-dark'), ('text-muted', 'text-muted'), ('text-primary', 'text-primary'), ('text-secondary', 'text-secondary'), ('text-warning', 'text-warning'), ('text-danger', 'text-danger'), ('text-success', 'text-success'), ('text-info', 'text-info')], default='text-white', max_length=100, verbose_name='Текст'),
        ),
    ]
