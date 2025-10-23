from django.urls import path, include
from Study_Buddy.views import (UserListView, UserDetailView, AssignmentListView, MaterialsListView, UserBaseView, assignment_counts_chart, AssignmentCreateView)
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
]
