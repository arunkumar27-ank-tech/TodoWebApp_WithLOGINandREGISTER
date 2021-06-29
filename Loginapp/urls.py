from django.urls import path
from django.urls.resolvers import URLPattern
from . views import CustomLoginView, detailView, taskUpdate, tasklist, TaskCreate, deleteTask,Registerpage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',Registerpage.as_view(), name='register'),


    path('',tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/',detailView.as_view(), name='task'),
    path('create/',TaskCreate.as_view(), name='create'),
    path('taskupdate/<int:pk>/',taskUpdate.as_view(), name='taskupdate'),
    path('taskdelete/<int:pk>/',deleteTask.as_view(), name='taskdelete'),
]
