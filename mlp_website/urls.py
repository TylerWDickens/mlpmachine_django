from django.urls import path
from mlp_website.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view())
]