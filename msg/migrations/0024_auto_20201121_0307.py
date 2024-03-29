# Generated by Django 3.1.2 on 2020-11-21 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg', '0023_auto_20201120_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='top',
            field=models.CharField(default='False', max_length=100, null=True, verbose_name='Закрепить'),
        ),
        migrations.AlterField(
            model_name='message',
            name='card_bg_color_choice',
            field=models.CharField(choices=[('bg-dark', 'Темный фон'), ('bg-light', 'Светлый фон'), ('bg-primary', 'Синий фон'), ('bg-secondary', 'Серый фон'), ('bg-success', 'Зеленый фон'), ('bg-danger', 'Красный фон'), ('bg-warning', 'Желтый фон'), ('bg-info', 'Голубой фон')], default='bg-dark', max_length=100, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='message',
            name='card_font_color_choice',
            field=models.CharField(choices=[('text-white', 'Белый текст'), ('text-dark', 'Темный текст'), ('text-muted', 'Приглушенный текст'), ('text-primary', 'Синий текст'), ('text-secondary', 'Серый текст'), ('text-warning', 'Желтый текст'), ('text-danger', 'Красный текст'), ('text-success', 'Зеленый цвет'), ('text-info', 'Голубой цвет')], default='text-white', max_length=100, verbose_name='Текст'),
        ),
    ]
