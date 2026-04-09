from django.urls import path
from .views import *

app_name = 'diary'

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('comments/', CommentView.as_view()),
]