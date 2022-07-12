from django.urls import path
import shop.views

urlpatterns = [
    path('', shop.views.home, name="homepage"),
    path('about/', shop.views.about, name="about"),
]