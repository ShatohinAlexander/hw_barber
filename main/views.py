from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from main.forms import ReviewForm, VisitForm
from main.models import Master, Review, Service

MENU = [
    {"title": "Главная", 'url': reverse_lazy("main_page")},
    {"title": "Отзыв", 'url': reverse_lazy("review_create")},
    {'title': 'Мастера', 'url': '#masters'},
    {'title': 'Услуги', 'url': '#services'},
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
        context['reviews'] = Review.objects.all()[:3]
        

        return context
    
class ThanksView(TemplateView):
    template_name = 'main/thanks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = MENU
        return context
    
    
class ReviewCreateView(CreateView):
    template_name = 'main/review_form.html'
    form_class = ReviewForm
    success_url = reverse_lazy("main_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        return context
    
