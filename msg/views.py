from django.shortcuts import render, redirect
from .models import Message, Comment, Privat
# from django.views.generic import ListView, DetailView
from .forms import MessageForm, CommentForm, PrivatForm
from django.contrib.auth.models import User
from django.utils import timezone

def msg(request):
    message = Message.objects.order_by('-id').all()
    error = ''
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            text=form.cleaned_data.get("text")
            user=form.cleaned_data.get("user")
            picture_file=form.cleaned_data.get("picture_file")
            card_bg_color_choice=form.cleaned_data.get("card_bg_color_choice")
            card_font_color_choice=form.cleaned_data.get("card_font_color_choice")
            print("\nНовость:")
            print("user: " + user + ", текст: " + text)
            print("picture: " + str(picture_file) +
                ", bg: " + card_bg_color_choice +
                ", font: " + card_font_color_choice + "\n")
            if request.user.is_authenticated:
                new.user = request.user.first_name
                new.admin_news = True
            new.save()
            return redirect('/msg')
        else:
            error = 'Ошибка',
    form = MessageForm()
    data = {
        'message': message,
        'form': form,
        'error': error,
    }
    return render(request, 'msg/msg.html', data)

# class MsgId(DetailView):
#     model = Message
#     template_name = 'msg/msg_id.html'
#     context_object_name = 'msg'

def msg_id(request, id):
    message = Message.objects.filter(id=id).all()
    comments = Comment.objects.filter(new=id).all()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment_form_save = form.save(commit=False)
            comment_form_save.new = Message.objects.get(id=id)
            comment_form_save.user = request.user
            text = form.cleaned_data.get("text")
            print("\nНовый коммент: ")
            print("текст: " + text + '\n')
            comment_form_save.save()
    form = CommentForm()
    data = {
        'message': message,
        'comments': comments,
        'form': form,
    }
    return render(request, 'msg/msg_id.html', data)



def privat(request):
    messages = Privat.objects.all()
    if request.method == "POST":
        form = PrivatForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            # message.text = form.cleaned_data.get("text")
            # print("\nПриватное сообщение."
            #     +"\nUser: "+message.user
            #     +", текст: "+message.text+'\n')
            message.save()
            return redirect('/msg/privat')
    form = PrivatForm()
    data = {
        'messages': messages,
        'form': form,
    }
    return render(request, 'msg/privat.html', data)
