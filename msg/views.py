from django.shortcuts import render, redirect
from .models import Message
from django.views.generic import ListView
from .forms import MessageForm
from django.contrib.auth.models import User

def msg(request):
    message = Message.objects.order_by('-id').all()
    error = ''
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        print(form['text'].value())
        if form.is_valid():
            if request.user.is_authenticated():
                form.user = username
            form.save()
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
