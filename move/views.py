from .models import Point_vente
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, TemplateView):
    model = Point_vente
    template_name = "index.html"
