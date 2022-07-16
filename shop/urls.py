from django.urls import path
from . import views
import shop.views

urlpatterns = [
    path('', shop.views.home, name="homepage"),
    path('about/', shop.views.about, name="about"),
    path('product/', shop.views.product, name="product"),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
]