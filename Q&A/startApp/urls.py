from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page, name='login_page'),
    path('chat/process_question/', views.process_question, name='process_question'),
    path('chat/', views.chat_page, name='chat_page'), 
]
