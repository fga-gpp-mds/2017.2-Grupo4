from django.conf.urls import url, include

from . import views

app_name = 'risk_rating'
urlpatterns = [
    url(r'^', views.risk_rating_view, name="risk_rating")
]