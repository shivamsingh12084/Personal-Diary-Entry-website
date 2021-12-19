from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView



# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class MainView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'learning_logs/title_list.html'


