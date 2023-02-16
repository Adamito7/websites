from django.shortcuts import render
from django.http import HttpResponse

from myapp.forms import LogForm
from myapp.forms import TimerForm

# Create your views here.

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form submission successful')        
    context = {'form': form}
    return render(request, 'home.html', context)

def timer_view(request):
    form = TimerForm()
    if request.method == 'POST':
        form = TimerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form submission successful')
    context = {"form": form}
    return render(request, 'timer.html',context)

