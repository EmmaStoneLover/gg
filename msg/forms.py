from .models import Message
from django.forms import ModelForm, TextInput, Select, Textarea, FileInput
from django import forms

class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ['text', 'user', 'picture', 'picture_file', 'card_bg_color_choice', 'card_font_color_choice']
        widgets = {
            'text': Textarea(attrs={
                'class': 'msg_input_text_and_bg_color form-control text-white bg-dark rounded',
                'placeholder': 'Текст',
                'rows':'4'
                }),
            'user': TextInput(attrs={
                'id': 'msg_input_user',
                'class': 'msg_input_text_and_bg_color form-control text-white bg-dark rounded',
                'placeholder': 'Отправитель',
                'value': ''
                }),
            'picture': TextInput(attrs={
                'class': 'msg_input_text_and_bg_color form-control text-white bg-dark rounded',
                'placeholder': 'Ссылка на изображение'
                }),
            'picture_file': FileInput(attrs={
                'id': 'msg_input_picture_file'
                }),
            'card_bg_color_choice': Select(attrs={
                'id': 'id_card_bg_color_choice',
                'class': 'msg_input_text_and_bg_color custom-select text-white bg-dark rounded'
                }),
            'card_font_color_choice': Select(attrs={
                'id': 'id_card_font_color_choice',
                'class': 'msg_input_text_and_bg_color custom-select text-white bg-dark rounded'
                })
        }
