from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('about/', views.about, name="about"),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name="product_page"),
]