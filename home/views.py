from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Tutorial
from .forms import TutorialForm
from django.shortcuts import render


def home(request):
    user = request.user
    return render(request, 'home.html', context={'user': user})


def list(request):
    queryset = Tutorial.objects.all()
    form = TutorialForm
    return render(
        request,
        "tutorial.html",
        {
            'tutorials': queryset,
        })


def createOrder(request):
    form = TutorialForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'form.html', context)
