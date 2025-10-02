
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import View
from Study_Buddy.models import User, Assignment, Materials
from django.views.generic import ListView, DetailView
from django.db.models import Count, Q
# Create your views here.


class UserBaseView(View):
    def get(self, request):
        return render(
            request,
            'users/user_base.html',
            context={'user_base_html': User.objects.all()}
        )

class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "user_rows_for_looping"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        q = self.request.GET.get("q")
        if q:
            search_qs = User.objects.filter(email__icontains=q)
        else:
            search_qs = None
        ctx["q"] = q
        ctx["search_results"] = search_qs
        ctx["total_users"] = User.objects.count()
        ctx["total_assignments"] = Assignment.objects.count()

        ctx["assignments_per_user"] = (
            User.objects
            .values("user_id", "email")
            .annotate(n_assignments=Count("assignments_related_name"))
        )
        ctx["materials_per_user"] = (
            User.objects
            .values("user_id", "email")
            .annotate(n_materials=Count("materials_related_name"))
        )
        return ctx
class AssignmentListView(ListView):
    model = Assignment
    template_name = "users/assignment_list.html"
    context_object_name = "assignment_rows_for_looping"

class MaterialsListView(ListView):
    model = Materials
    template_name = "users/material_list.html"
    context_object_name = "material_rows_for_looping"

class UserDetailView(DetailView):
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