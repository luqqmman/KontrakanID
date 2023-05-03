from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from forum.models import Rent, Comment


class MyRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'account/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} created successfully. Please log in.')
            return redirect('account:login')
        return render(request, 'account/register.html', {'form': form})
    

class MyLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('forum:index')
    
    def form_invalid(self, form):
        messages.warning(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

class MyProfile(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'account/profile.html'
    context_object_name = 'user'

    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')
    

class MyRent(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Rent
    template_name = 'account/my_rent.html'
    context_object_name = 'rents'
    ordering = ['-date_posted']

    def get_queryset(self):
        account = User.objects.get(pk=self.kwargs.get('pk'))
        return account.own.all()
    
    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')
    

class MyComment(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Comment
    template_name = 'account/my_comment.html'
    context_object_name = 'comments'
    ordering = ['-date_posted']

    def get_queryset(self):
        account = User.objects.get(pk=self.kwargs.get('pk'))
        return account.comment.all()
    
    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')
    

class MyWaitingList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Rent
    template_name = 'account/my_waiting_list.html'
    context_object_name = 'waiting_list'
    ordering = ['-date_posted']

    def get_queryset(self):
        account = User.objects.get(pk=self.kwargs.get('pk'))
        return account.waiting_list.all()
    
    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')


