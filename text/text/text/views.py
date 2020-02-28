from django.http import HttpResponse
from django.shortcuts import render
#use of url
# def index(request):
#     return HttpResponse('''<h1>hello Prabeena....</h1><a href="https://www.tutorialspoint.com/django/django_overview.htm">django website </a>''')
# def about(request):
#     return HttpResponse("software engineer....")

#templates
def index(request):
   return render(request,'index.html')
def analyze(request):
   tex=request.GET.get("text", 'default')
   print(tex)#it will print the value passed in the box
   ana = request.GET.get("remove", 'default')
   print(ana)
   return HttpResponse("remove punc")

#use of pipeline
# def home(request):
#     #return HttpResponse("home")
#     return HttpResponse('''<h1>home</h1> <a href="http://127.0.0.1:8000/cap">cap </a>''')
# def capitalise(request):
#     #return HttpResponse("capitalise")
#     return HttpResponse('''<h1>capitalise</h1> <a href='/'>back</a> <a href="http://127.0.0.1:8000/space">space </a>''')
# def spaceremove(request):
#     #return HttpResponse("space remove")
#     return HttpResponse('''<h1>space remove</h1> <a href='/'>back</a> <a href="http://127.0.0.1:8000/line">line </a>''')
# def newline(request):
#     return HttpResponse('''<h1>new line</h1>  <a href='/'>back</a>''')
