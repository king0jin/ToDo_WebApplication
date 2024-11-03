from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#CRUD작업 - 사용하고 싶은 테이블(모델) 불어오기
from .models import Todo

# Create your views here.

#1. CRUD -  데이터 조회
def TodoView(request):
    data = Todo.objects.all()
    print(data)
    return render(request, 'TodoView.html', {'data':data})

#2. CRUD -  데이터 삽입
@csrf_exempt
def TodoInsert(request):
    if request.method == 'POST':
        # 요청에서 JSON 데이터를 파싱합니다.
        data = json.loads(request.body)
        # Todo 모델에 새 데이터를 추가합니다.
        new_todo = Todo.objects.create(
            id=data.get('id'),
            userid=data.get('userid'),
            title=data.get('title'),
            isdone=data.get('isdone'),
            untildate=data.get('untildate')
        )
        # JSON 응답으로 새로 추가된 데이터를 반환합니다.
        return JsonResponse({'id': new_todo.id, 'message': 'Todo가 추가되었습니다.'})
    return render(request, "TodoInsert.html")