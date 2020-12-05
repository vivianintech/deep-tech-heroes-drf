from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/new/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('users/becomehost/', views.HostUserList.as_view()),
    path('users/becomehero/', views.HeroUserList.as_view()),
    path('users/hero/<int:pk>/', views.HeroUserDetail.as_view()),
    path('users/<int:pk>/heroupgrade/', views.HeroUpgradeList.as_view()),
    path('users/host/<int:pk>/', views.HostUserDetail.as_view()),
    path('users/<int:pk>/hostupgrade/', views.HostUpgradeList.as_view()),
    path('users/heros/', views.HeroUserList.as_view()),
    path('users/hosts/', views.HostUserList.as_view()),
    path('heroes/', views.HeroList.as_view()),
    path('hosts/', views.HostList.as_view()),
    path('users/heroes/feminine/', views.FeminineHeroList.as_view()),
    path('users/heroes/nongender/', views.NonGenderHeroList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)