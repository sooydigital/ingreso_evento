from django.urls import path, include

# importing views from views..py
from myapp import views
from django.views.generic import TemplateView
from django.urls import path


app_name = "app"
urlpatterns = [
    path('activate/', TemplateView.as_view(template_name="activation_form.html"),  name='activation_forms'),
    path('welcome/', TemplateView.as_view(template_name="welcome.html"), name='welcome')
]




