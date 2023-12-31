from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('types', views.create_types_page),
    path('types/<sign_types>', views.get_info_in_types, name='types-name'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),


]