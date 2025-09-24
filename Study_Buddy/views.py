
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import User
# Create your views here.

def user_list_view(request):
    users = User.objects.all()
    template = loader.get_template("users/user_list.html")
    context = {"users": users}
    output = template.render(context, request)
    return HttpResponse(output)

def user_list_render(request):
    users = User.objects.all()
    context = {"user_list_html": users}
    return render(request, "users/user_list.html", context)