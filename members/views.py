from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Testing testing, 1,2,3</h1>")