from django.urls import path
from . import views

app_name = 'investment'

urlpatterns = [
    path('ideas/', views.ideas, name='ideas'),
    path('ideas/<int:pk>/', views.idea, name='idea'),
    path('idea/create/', views.idea_create, name='idea_create'),
    path('idea/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('my-ideas/', views.my_ideas, name='my_ideas'),
    path('idea/<int:pk>/delete', views.idea_delete, name='idea_delete')
]