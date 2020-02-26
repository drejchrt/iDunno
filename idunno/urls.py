from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_question', views.add_question, name='add_question'),
    path('list/<str:sort_attr>', views.list, name='list'),
    path('game/<str:color>',views.game, name='game'),
    path('<int:question_id>/', views.question, name='question'),
    path('<int:question_id>/edit', views.edit_question, name='edit'),
    path('search/<str:query>', views.search, name='search')
]
