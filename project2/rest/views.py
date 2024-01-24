from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CarForm
# Create your views here.
class postCarData(TemplateView):
    template_name = "rest/t1.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = CarForm
        context['endpoint'] = "http://127.0.0.1:8000/api/Cars/"
        return context

