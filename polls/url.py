from django.urls import path

from .import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('question/', views.questionList, name='question'),
    path('question/<int:pk>/', views.questionDetail, name='question-detail'),
    path('question-create/', views.questionCreate, name='question-create'),
    path('question-update/<int:pk>/', views.questionUpdate, name='question-update'),
    path('question-delete/<int:pk>/', views.questionDelete, name='question-delete'),

]