from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('budget/', views.budget, name='budget'),
    path('accounts/', views.accounts, name='accounts'),
    path('<int:item_id>/', views.budget_item, name="details"),
]
