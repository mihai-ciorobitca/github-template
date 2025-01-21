from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if username == 'admin' and password == 'password':
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'home.html')
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/login.html')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})