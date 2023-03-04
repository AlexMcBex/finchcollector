from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_index, name='index'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finch_update"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finch_delete"),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:finch_id>/add_ribbon/', views.add_ribbon, name='add_ribbon'),
    path('finches/<int:finch_id>', views.finch_detail, name='detail'),
    path('nests/', views.NestList.as_view(), name='nests_index'),
    path('nests/create/', views.NestCreate.as_view(), name='nests_create'),
    path('nests/<int:pk>/update/', views.NestUpdate.as_view(), name='nests_update'),
    path('nests/<int:pk>/delete/', views.NestDelete.as_view(), name='nests_delete'),
    path('nests/<int:pk>/', views.NestDetail.as_view(), name='nests_detail'),
]
