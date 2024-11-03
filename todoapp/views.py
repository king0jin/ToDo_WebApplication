from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
#CRUD작업 - 사용하고 싶은 테이블(모델) 불어오기
from todoapp.models import Todo
#CURD작업 - 특정 필드의 최대값을 가져오기 위해 사용
from django.db.models import Max
#CURD작업 - JSON데이터 처리를 위해 사용
import json
#CRUD작업 - HTTP 요청을 처리하는 도중에 특정 URL로 사용자를 리디렉션하기 위해 사용
from django.shortcuts import redirect
# Create your views here.

#1. CRUD -  데이터 조회
def TodoView(request):
    data = Todo.objects.all()
    print(data)
    return render(request, 'TodoView.html', {'data':data})