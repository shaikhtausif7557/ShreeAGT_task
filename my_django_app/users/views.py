from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_data')
    else:
        form = UserForm()
    return render(request, 'users/form.html', {'form': form})

def user_data(request):
    users = User.objects.all()
    return render(request, 'users/data.html', {'users': users})