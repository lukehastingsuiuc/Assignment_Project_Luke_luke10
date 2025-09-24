
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from .models import User
# Create your views here.

def user_list_view(request):
    users = User.objects.all()
    context = {"users": users}
    template = loader.get_template("users/user_list.html")
    output = template.render(context)
    return HttpResponse(output)

def user_list_render(request):
    users = User.objects.all()
    context = {"user_list_html": users}
    return render(request, "users/user_list.html", context)

class UserDetail(View):
    def get(self, request, primary_key):
        user = get_object_or_404(User, pk=primary_key)
        assignments = user.assignments_related_name.all()
        return render(
            request,
            'users/user_detail.html',
            {
                'single_user_var_for_looping': user,
                'assignments_var_for_looping': assignments,
            },
        )