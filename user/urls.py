from django.urls import path
from . import views
urlpatterns = [

    path('', views.all_posts_view, name='all_maqola'),
    path('post/search', views.search, name='search'),
    path('post/<int:pk>/', views.maqola_view, name='maqola_detail'),
    path('post/tabletka/<int:pk>/', views.tabletka_view, name='tabletka_detail'),
# add post
    path('post/add/', views.add_maqola, name='add_maqola'),
    path('post/add/add/', views.add_add_maqola, name='add_add'),
# change
    path('post/<int:pk>/change/', views.change_maqola, name='change_maqola'),
    path('post/<int:pk>/change/change/', views.change_change_maqola, name='change_change'),
# delete
    path('post/<int:pk>/delete/', views.DeleteMaqolaView.as_view(), name='delete_maqola'),
# registration
    path('signup/', views.signup, name='signup'),
    path('signup/check_code/', views.check_code, name='check_code'),
    path('signup/hamshira/', views.add_nurse, name='signup_hamshira'),
    path('signup/nurse_check_code/' ,views.check_code_hamshira,name='nurse_check_code'),
    path('dorilar_view/',views.dorilar_view,name='dorilar_url'),
    path('maqolalar_view/',views.maqolalar_view,name='maqolalar_view')

]