from django.shortcuts import render
from django.views.generic import TemplateView


# Create your models here.
class HomePageView(TemplateView):

    template_name = "mlp_website/landing.html"
