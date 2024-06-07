from django.urls import path

from . import views


urlpatterns = [
    path("", views.RequestCatcherView.as_view()),
]

