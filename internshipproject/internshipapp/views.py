from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import travel, team


# Create your views here.
#def demo(request):
 #   return render(request,"home.html")
#def about(request):
 #  return render(request,'about.html')
#def data(request):
 #   return render(request,"data.html")
#def p(request):      #passing value
   # name="buddy"
   # return render(request,"p.html",{'a':'buddy'})
#def demo1(request):
 #return render(request,"demo1.html")
#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res=x+y
    #return render(request,"result.html",{'result':res})
#def demo2(request):
 #   return render(request,"demo2.html")
#def operation(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # add=x+y
    #sub=x-y
    #mul=x*y
    #div=x//y
    #return render(request,"operation.html",{'result1':add,'result2':sub,'result3':mul,'result4':div})



    #new project................................................................................
def project(request):
    obj=travel.objects.all()
    tea=team.objects.all()
    return render(request,"index.html",{'result':obj,'output':tea})





