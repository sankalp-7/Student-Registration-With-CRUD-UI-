import imp
from django.urls import path
from . import views
app_name='student'
urlpatterns=[
    path('',views.Home.as_view(),name='home'),
    path('add/',views.FormView.as_view(),name='form'),
    path('update/<int:pk>',views.Update.as_view(),name='update'),
    path('delete/<int:pk>',views.Delete.as_view(),name='delete'),
]