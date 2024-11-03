from django.urls import path

#ajax요청 추가
from .views import TodoView, TodoInsert

urlpatterns = [
    #1. CRUD - todo요청시, TodoView 호출
    path('todo/', TodoView),
    #2. CRUD - todoajax요청시, TodoInsert 호출
    path('todoajax/', TodoInsert)
]