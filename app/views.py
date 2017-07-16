from django.shortcuts import render, HttpResponse,redirect

# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    return render(request, 'index.html')


def login(request):
    from django.contrib.auth import authenticate, login
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            login_err = 'cuowu '
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


