from django.shortcuts import render, redirect
import pyshorteners
from django.http import HttpResponseRedirect
from django.contrib import messages

def index(request):
    short_url = ''
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        return HttpResponseRedirect('/?short_url='+short_url)
    return render(request, 'urlapp/index.html', {"short_url": short_url})
