from django.shortcuts import render, redirect
from .models import Widget

# Create your views here.

def dashboard(request):
    widgets = Widget.objects.all().order_by('position')
    return render(request, 'dashboard/index.html', {'widgets': widgets})

def add_widget(request):
    if request.method == 'POST':
        widget_type = request.POST.get('widget_type')
        Widget.objects.create(widget_type=widget_type)
    return redirect('dashboard')

def delete_widget(request, widget_id):
    if request.method == 'POST':
        Widget.objects.filter(id=widget_id).delete()
    return redirect('dashboard')