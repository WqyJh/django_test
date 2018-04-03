from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from .models import User


def index(request):
    return render(request, 'index.html')


def create_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create(username=username, password=password)
    text = 'success' if user else 'fail'
    return HttpResponse(text)


def get_user(request):
    users = User.objects.all()
    data = [{'username': user.username, 'password': user.password} for user in users]
    return JsonResponse(data, safe=False)


def delete_user(request):
    username = request.GET['username']
    user = User.objects.get(username=username).delete()
    text = 'success' if user else 'fail'
    return HttpResponse(text)
