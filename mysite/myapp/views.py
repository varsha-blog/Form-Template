# myapp/views.py
from .form import *
from django.http import HttpResponse
from django.shortcuts import render


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['name']
            context = {'msg': '<span style="color: green;">Thank you</span>', 'name': user}
        return render(request, "home.html", context)
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

