from django.contrib.auth.signals import user_login_failed
from Loginapp import models
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from . models import Todo

class CustomLoginView(LoginView):
    template_name = 'loginapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class Registerpage(FormView):
    template_name = 'loginapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registerpage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Registerpage, self).get( *args, **kwargs)



class tasklist(LoginRequiredMixin,ListView):
    model = Todo
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input

        return context

    
class detailView(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'task'
    template_name = 'loginapp/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class taskUpdate(LoginRequiredMixin,UpdateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')


class deleteTask(LoginRequiredMixin,DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


