from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'Login.html', context)

    elif request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)
            # Redirect to a success page.
            return redirect('/admin')

        else:
            # Return an 'invalid login' error message.
            form = AuthenticationForm(data=request.POST)
            context = {'form': form}
            return render(request, 'Login.html', context)

# Create your views here.
def create_person(request):

    form = UserCreationForm
    context = {'form': form}

    return render(request, 'register.html', context)

def logout_view(request):

    logout(request)

    return redirect('/login')