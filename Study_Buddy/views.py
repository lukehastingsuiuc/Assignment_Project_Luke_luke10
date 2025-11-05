from urllib import request

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import View
from Study_Buddy.models import User, Assignment, Materials
from django.views.generic import ListView, DetailView
from django.db.models import Count, Q
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
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
            .annotate(n_assignments=Count("assignments_related_name")).order_by("-n_assignments")
        )
        ctx["materials_per_user"] = (
            User.objects
            .values("user_id", "email")
            .annotate(n_materials=Count("materials_related_name"))
        )
        return ctx
class AssignmentListView(ListView):
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


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

def assignment_counts_chart(request):
    data = (
        User.objects
        .annotate(assignment_count=Count("assignments_related_name"))
        .order_by("email")
    )
    labels = [user.email for user in data]
    counts = [user.assignment_count for user in data]

    fig, ax = plt.subplots(figsize=(6, 3), dpi=150)

    ax.bar(labels, counts, color="#13294B")
    ax.set_title("Assignments per User", fontsize=10, color="#13294B")

    ax.set_xlabel("User", fontsize=8)
    ax.set_ylabel("Assignments", fontsize=8)

    ax.tick_params(axis="x", rotation=45, labelsize=8)
    ax.tick_params(axis="y", labelsize=8)

    fig.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format="png")

    plt.close(fig)
    buf.seek(0)

    return HttpResponse(buf.getvalue(), content_type="image/png")

from django.shortcuts import redirect
from .forms import AssignmentForm

def add_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("assignment-list-url")
    else:
        form = AssignmentForm()
    return render(request, "users/add_assignment.html", {"form": form})

from django.views.generic import CreateView
from django.urls import reverse_lazy

class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "users/add_assignment.html"
    success_url = reverse_lazy("assignment-list-url")

from django.http import JsonResponse
from django.db.models import Count, Q



class UsersAPI(View):
    def get(self, request):
        q = (request.GET.get("q") or "").strip()
        qs = User.objects.all()
        if q:
            qs = qs.filter(Q(email__icontains=q))
        data = (list(qs.values("email", "user_id").order_by("email")))
        return JsonResponse({"count": len(data), "results": data})

def api_assignments_per_user(request):
    rows = (
        User.objects
        .annotate(n_assignments=Count("assignments_related_name"))
    .values("email", "n_assignments")
    .order_by("n_assignments")
    )
    return JsonResponse({"results": list(rows)})

import json
import urllib.request
from django.urls import reverse
from django.views.generic import TemplateView

class AssignmentsChartPage(TemplateView):
    template_name = "users/assignments_chart.html"

def assignments_chart_png(request):
    api_url = request.build_absolute_uri(reverse("api-assignments-per-user"))
    with urllib.request.urlopen(api_url) as resp:
        payload = json.load(resp)
    rows = payload.get("results", [])
    labels = [r["email"] for r in rows]
    counts = [r["n_assignments"] for r in rows]
    x = range(len(labels))
    width = 0.4
    fig, ax = plt.subplots(figsize=(6, 3), dpi=150)
    ax.bar([i - width/2 for i in x], counts, width=width, color="#13294B")
    ax.set_title("Assignments per User")
    ax.set_ylabel("Assignments")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.legend()
    fig.tight_layout()
    buf=BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)

    return HttpResponse(buf.getvalue(), content_type="image/png")

def api_ping_json(request):
    return JsonResponse({"ok": True})
def api_ping_httpresponse(request):
    return HttpResponse("ok: true", content_type="text/plain")

import requests


class PokemonDemo(View):
    def get(self, request):
        q = self.request.GET.get("q")
        params = {
        }
        try:
            output_raw_all = requests.get("https://pokeapi.co/api/v2/pokemon/"+ q, params=params, timeout=5)
            output_raw_all.raise_for_status()
            output_polished_all = output_raw_all.json()
            output_polished_name_only = output_polished_all.get("name", {})
            output_polished_types_only = output_polished_all.get("types", {})
            output_polished_height_only = output_polished_all.get("height", {})
            output_polished_weight_only = output_polished_all.get("weight", {})
            return JsonResponse({"ok": True, "name": output_polished_name_only, "types": output_polished_types_only, "height": output_polished_height_only, "weight": output_polished_weight_only,})
        except requests.exceptions.RequestException as e:
            return JsonResponse({"ok": False, "error": str(e)}, status=502)

