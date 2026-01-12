from .models import Point_vente
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from .serializers import PointSerializer

class HomePageView(TemplateView):
    model = Point_vente
    template_name = "index.html"

class PointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Point_vente.objects.all()
    serializer_class = PointSerializer
