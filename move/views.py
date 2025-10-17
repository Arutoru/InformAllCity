from .models import Point_vente
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    model = Point_vente
    template_name = "index.html"
