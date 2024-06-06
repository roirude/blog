from django.urls import path

from article import views

urlpatterns = [
    path('',views.list_article,name='list_article'),
    path('add_article/', views.add_article, name='add_article'),
    path('article/<int:id>/',views.article, name='article'),
    path('article/<int:id>/update/', views.article_update, name='article_update'),
    path('article/<int:id>/delete/', views.article_delete, name='article_delete'),
]
