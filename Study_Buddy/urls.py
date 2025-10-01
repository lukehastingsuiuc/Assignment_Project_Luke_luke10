from django.urls import path, include
from Study_Buddy.views import (UserListView, UserDetail, AssignmentListView, MaterialsListView)

urlpatterns = [
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
         UserDetail.as_view(),
         name='user-detail-url'),
]