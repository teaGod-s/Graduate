from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'test.html')


def home(request):
    # string = "因为我是天才啊"
    # TutorialList = ["HTML", "CSS", "JQuery", "Python", "Giango"]
    # info_dict = {'site': '第一个字典的值', 'content': '第二个字典的值'}

    # List = map(str, range(100))
    # return render(request, 'test.html', {'List': List})
    return render(request, "zhu.html")


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))



