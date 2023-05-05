# from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect,HttpResponse


# Create your views here.
@login_required
def index(request):
    return HttpResponse(request.user)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # 注册成功后重定向到主页或其他页面
    else:
        form = UserCreationForm()
    return render(request, 'recipe/register.html', {'form': form})
