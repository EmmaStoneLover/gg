from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.CharField('Пользователь', max_length=120)
    text = models.CharField('Текст', max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    picture = models.CharField('Изображение', blank=True, null=True, max_length=100, default='none')
    picture_file = models.ImageField('Загрузка пикчи', upload_to='msg', blank=True, max_length=200, default='none')
    BG_COLOR_CHOICE = [
        ('bg-dark', 'Темный фон'),
        ('bg-light', 'Светлый фон'),
        ('bg-primary','Синий фон'),
        ('bg-success', 'Зеленый фон'),
        ('bg-danger', 'Красный фон'),
        ('bg-warning', 'Желтый фон'),
        ('bg-info', 'Голубой фон')]
    card_bg_color_choice = models.CharField('Цвет фона', max_length=100, choices=BG_COLOR_CHOICE, default='bg-dark')
    FONT_COLOR_CHOICE = [
        ('text-white', 'Белый текст'),
        ('text-dark', 'Темный текст'),
        ('text-primary', 'Синий текст'),
        ('text-secondary', 'Серый текст'),
        ('text-warning', 'Желтый текст'),
        ('text-danger', 'Красный текст'),
        ('text-success', 'Зеленый цвет'),
        ('text-info', 'Голубой цвет')]
    card_font_color_choice = models.CharField('Цвет текста', max_length=100, choices=FONT_COLOR_CHOICE, default='text-white')
    PINNED_NEWS = [('False','Не закреплена'), ('True','Закрепить'), ('None','Скрытая')]
    top = models.CharField('Закрепить', blank=True, null=True, max_length=100, choices=PINNED_NEWS, default='False')
    admin_news = models.BooleanField('Новости сайта', default='False')


    def __str__(self):
        return 'id: ' + str(self.id) + ', ' + self.text

    # Название модели в админке
    class Meta():
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new = models.ForeignKey(Message, on_delete=models.CASCADE)
    text = models.CharField('Текст', max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ', ' + str(self.new.id) + ', ' + self.user.first_name + ', '+ self.text

    # Название модели в админке
    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
