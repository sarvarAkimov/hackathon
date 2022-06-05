from django.urls import path, include
from . import views
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.singin, name='singin'),
    path('chat/<int:pk>/',views.chat,name='chat'),
    path('chat_add/',views.add_chat,name='add_chat'),
    path('times/<str:type>/',views.times,name='times'),
    path('time/', views.time, name='time'),
    path('time_data_add/',views.time_data_add,name='time_data_add'),
    path('chatting/',views.chatting,name='chatting'),
    path('chats/',views.Chats,name='chats'),
    path('see/',views.See,name='see'),
    path('seeing/',views.Seeing,name='seeing'),
    path('time_data_add2/',views.time_data_add2,name='time_data_add2'),
    path('close_chat',views.close_chat,name='close_chat'),
    path('xamshiras/',views.statistic,name='xamshiras'),
    path('statistics_user/<int:pk>/',views.static_user,name='statistics_xamshira'),
    path('add_followers/<int:pk>/',views.add_followers,name='add_followers'),
    path('add_like/<int:pk>/',views.add_like,name='add_like')
]