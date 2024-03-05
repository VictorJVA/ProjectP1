from django.shortcuts import render, redirect
def home(request):
    return render(request, "hello/home.html")
def about(request):
    return render(request, "hello/about.html")