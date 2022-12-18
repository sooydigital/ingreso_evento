from django.urls import path, include

# importing views from views..py
from myapp import views
from django.views.generic import TemplateView
from django.urls import path
from myapp import views

app_name = "app"
urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"),  name='test'),
    path('api/validate', views.validate, name='validate' )
]




