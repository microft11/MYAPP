from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">你好我是雷电霸王龙</h1>'
    return HttpResponse(line1)
