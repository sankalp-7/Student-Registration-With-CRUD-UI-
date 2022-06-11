from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,UpdateView,DeleteView
from . import models
class FormView(CreateView):
    model=models.StudentModel
    fields="__all__"
    success_url="/student/"
class Home(ListView):
    model=models.StudentModel
    context_object_name='student_list'
class Update(UpdateView):
    model=models.StudentModel
    fields="__all__"
    success_url="/student/"
class Delete(DeleteView):
    model=models.StudentModel
    success_url="/student/"
