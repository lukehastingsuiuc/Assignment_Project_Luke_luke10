from django.urls import path, include
from Study_Buddy.views import (UserListView, UserDetailView, AssignmentListView, MaterialsListView, UserBaseView,
                               assignment_counts_chart, AssignmentCreateView, UsersAPI, assignments_chart_png,
                               AssignmentsChartPage, PokemonDemo)
from . import views
urlpatterns = [
    path('base/',
         UserBaseView.as_view(),
         name="user-base-url"),

    path('user/',
         UserListView.as_view(),
         name='user-list-url'),

    path('assignment/',
        AssignmentListView.as_view(),
        name='assignment-list-url'),

    path('material/',
         MaterialsListView.as_view(),
         name='material-list-url'),

    path('user/<int:primary_key>/',
         UserDetailView.as_view(),
         name='user-detail-url'),

    path("charts/users.png",
         assignment_counts_chart,  # FUNCTION VIEW
         name="chart-users"),

    path("function-add-assignment/", views.add_assignment, name="function-add-assignment-url"),

    path("class-add-assignment/", AssignmentCreateView.as_view(), name="class-add-assignment-url"),

    path("api/users", UsersAPI.as_view(), name="api-users"),
    path("api/assignments-per-user", views.api_assignments_per_user, name="api-assignments-per-user"),

    path("charts/assignments/", AssignmentsChartPage.as_view(), name="assignments-chart-page"),
    path("charts/assignments.png", assignments_chart_png, name="assignments-chart-png"),
    path("api/ping-httpresponse/", views.api_ping_httpresponse, name="api-ping-httpresponse"),
    path("api/ping-json/", views.api_ping_json, name="api-ping-json"),
    path("api/pokemon/", PokemonDemo.as_view(), name="api-pokemon"),
]
