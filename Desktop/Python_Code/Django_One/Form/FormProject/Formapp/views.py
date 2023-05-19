from django.shortcuts import render, redirect
from .models import Formapp
from .forms import FormappForm

def HomePageView(request):
    all_post = Formapp.objects.all()
    context = {"all_post": all_post}
    return render(request, 'index.html', context)

def index(request):
    if request.method == 'POST':
        form = FormappForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormappForm()
    
    context = {'form': form}
    return render(request, 'index.html', context)