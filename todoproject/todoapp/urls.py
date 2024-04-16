from . import views
from django.urls import path

urlpatterns = [
    path("", views.addTask, name='addTask'),
    path("delete/<int:taskid>/", views.deleteTask, name='deleteTask'),
    path("update/<int:id>", views.updateTask, name='updateTask'),

    # for class based views
    path("cbvhome/", views.TaskListView.as_view(), name='cbvhome'),
    path("cbvdetail/<int:pk>/", views.TaskDetailView.as_view(), name='cbvdetail'),
    path("cbvupdate/<int:pk>/", views.TaskUpdateView.as_view(), name='cbvupdate'),
    path("cbvdelete/<int:pk>/", views.TaskDeleteView.as_view(), name='cbvdelete'),
]