from django.urls import path, include
from Study_Buddy.views import (UserListView, UserDetailView, AssignmentListView, MaterialsListView, UserBaseView)

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
]