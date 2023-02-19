from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# index 요청
def index(request):
    # 중간에 비즈니스 로직
    return HttpResponse("Hello, world. You are at the polls index")


def test(request):
    return HttpResponse("Hello, world. You are at the test index")
