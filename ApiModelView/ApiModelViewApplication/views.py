from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    return HttpResponse("<h1>hello django</h1>")

def learn_python(request):
    param="learn python"
    a=16.652
    b=22.252
    c=35.5655
    d=42.22
    dec={'Apple':a,'Ball':b,'Cat':c,'Dog':d}
    return render(request,'index.html',{'params':dec}) 


def learn_python(request):
    param="learn python"
    params='learn django'
    
    return render(request,'index.html',{'param':"learn python","params":'learn django'}) 

def learn_js(request):
    param="learn python"
    params='learn django'

    return render(request,'condition.html',{'param':"learn web dev 1","params":'learn js 2'}) 

def dictonary(request):
    data={'stu1':{'name':'sanjay', 'roll':1},
          'stu2':{'name':'sandeep', 'roll':2},
          'stu3':{'name':'santosh', 'roll':3},
          'stu4':{'name':'kusum', 'roll':4},
          'stu5':{'name':'bootan ji', 'roll':5},
          'stu6':{'name':'sadika ji', 'roll':6},
    
    }
    return render (request,'dictonary.html',{'datas':data})