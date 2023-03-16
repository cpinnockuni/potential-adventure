from django.urls import path
from . import views

urlpatterns =[

    path("", views.home, name="home"),
    path("community/", views.community, name="community"),
     path("studentlife/", views.studentlife, name="studentlife"),
     path("howto/", views.howto, name="howto"),
     path("information/", views.information, name="information"),
     path("services/", views.services, name="services"),
     path('login/', views.login_view, name = 'login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]