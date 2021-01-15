from django.shortcuts import render, redirect
from .models import Message, Comment
# from django.views.generic import ListView, DetailView
from .forms import MessageForm, CommentForm
from django.contrib.auth.models import User

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
                ", font: " + card_font_color_choice + "\n"
            )

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
        'error': error
    }
    return render(request, 'msg/msg.html', data)



def privat(request):
    smth = "Пошел нахуй спать!"
    data = {
        'smth': smth
    }
    return render(request, 'msg/privat.html', data)



# class MsgId(DetailView):
#     model = Message
#     template_name = 'msg/msg_id.html'
#     context_object_name = 'msg'



def msg_id(request, id):
    message = Message.objects.filter(id=id).all()
    print(message)
    comments = Comment.objects.filter(new=id).all()
    print(comments)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment_form_save = form.save(commit=False)
            comment_form_save.new = Message.objects.get(id=id)
            comment_form_save.user = request.user
             
            # text=form.cleaned_data.get("text")
            # user=form.cleaned_data.get("user")
            # print("Новый коммент: ")
            # print("user: " + user + ", текст: " + text)

            comment_form_save.save()
    form = CommentForm()
    data = {
        'message': message,
        'comments': comments,
        'form': form,
    }
    return render(request, 'msg/msg_id.html', data)
