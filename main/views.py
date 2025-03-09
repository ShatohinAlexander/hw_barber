from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

from main.forms import ReviewForm, VisitForm
from main.models import Master, Service, Visit

MENU = [
    {"title": "Главная", "url": reverse_lazy("main:main_page")},
    {'title': 'Мастера', 'url': '#masters'},
    {'title': 'Услуги', 'url': '#services'},
    {'title': 'Записи', 'url': reverse_lazy("main:visit_list")},
    {'title': 'Отзыв', 'url': reverse_lazy("main:review_create")},
    {'title': 'Запись на стрижку', 'url': '#orderForm'},
]

class MainPageView(CreateView):
    template_name = "main/index.html"
    form_class = VisitForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU
        context["masters"] = Master.objects.all()
        context['services'] = Service.objects.all()

        return context
    
class ThanksView(TemplateView):
    template_name = 'main/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU
        return context
    
