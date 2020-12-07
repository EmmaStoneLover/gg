from django.shortcuts import render, redirect
from .models import Message
from django.views.generic import ListView
from .forms import MessageForm

def msg(request):
    message = Message.objects.order_by('-id').all()
    error = ''
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
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
