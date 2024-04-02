from django.shortcuts import render
def curd(request):
    return render(request,'curd.html',context={'name':'curd'})
# Create your views here.
