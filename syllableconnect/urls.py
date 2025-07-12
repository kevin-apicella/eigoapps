from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_app_syllableconnect, name="syllable_connect"),
    path('check-answer', views.check_answer, name='check_answer'),
    path('previous', views.load_previous_question, name='previous'),
    path('next', views.load_next_question, name='next')
]