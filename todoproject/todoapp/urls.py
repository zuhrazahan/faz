from django.urls import path
from . import views

app_name = 'todoapp'

from todoproject import settings

urlpatterns = [

    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:tid>/', views.update, name='update'),
    path('cbvhome/', views.Tasklistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.Taskdetailviews.as_view(), name='detail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')

]
