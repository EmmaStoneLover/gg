from .models import Message, Comment, Privat
from django.forms import ModelForm, TextInput, Select, Textarea, FileInput
from django import forms

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'user', 'picture_file',
            'card_bg_color_choice', 'card_font_color_choice']
        widgets = {
            'text': Textarea(attrs={
                'class': 'msg_input_text_and_bg_color form-control pl-md-4 pl-lg-3 text-white bg-dark rounded',
                'placeholder': 'Вставить text',
                'rows':'4',
                'v-model': 'vue_text',
                }),
            'user': TextInput(attrs={
                'id': 'msg_input_user',
                'class': 'msg_input_text_and_bg_color form-control pl-md-4 pl-lg-3 text-white bg-dark rounded',
                'placeholder': 'Кто такой, чем известен?',
                'v-model': 'vue_user',
                }),
            # 'picture': TextInput(attrs={
            #     'class': 'msg_input_text_and_bg_color form-control text-white bg-dark rounded',
            #     'placeholder': 'Ссылка на изображение',
            #     }),
            'picture_file': FileInput(attrs={
                'id': 'msg_input_picture_file',
                'onchange': 'input_image_onchange(files)'
                }),
            'card_bg_color_choice': Select(attrs={
                'id': 'id_card_bg_color_choice',
                'class': 'msg_input_text_and_bg_color form-select text-white bg-dark pl-md-4 pl-lg-3 rounded',
                'v-model': 'vue_card_bg_color_choice',
                }),
            'card_font_color_choice': Select(attrs={
                'id': 'id_card_font_color_choice',
                'class': 'msg_input_text_and_bg_color form-select text-white bg-dark pl-md-4 pl-lg-3 rounded',
                'v-model': 'vue_card_font_color_choice',
                })
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': TextInput(attrs={
            'class': 'form-control bg-dark text-white p-md-3 p-lg-2 mb-md-4 mb-lg-2 rounded',
            'placeholder': 'Оставить комментарияй'
        })}

class PrivatForm(ModelForm):
    class Meta:
        model = Privat
        fields = ['text']
        widgets = {'text': TextInput(attrs={
            'class': 'form-control bg-dark text-white pl-4',
            'placeholder': 'Написать'
        })}
