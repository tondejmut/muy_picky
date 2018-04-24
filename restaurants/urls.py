from django.conf.urls import url
from django.views.generic import TemplateView
from .views import (
    restaurant_listview,
    RestaurantListView,
    SearchRestaurantListView,
)
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    url(r'^restaurants/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),
 #  url(r'^restaurants/fast-food/$', FastFoodRestaurantListView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
]
