from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Course,Student
from django.contrib import messages

def show(request):
    data=Student.objects.filter (isdelete = False)
    return render(request,'home.html',{'a':data})

def form(request):
     if request.method=="POST":
          data=(request.POST)
          n=data['name']
          a=data['age']
          e=data['email']
          ad=data['address']
          var= Student(name=n,age=a,email=e,address=ad)
          var.save()
          messages.success(request,"SUCCESS")
          return redirect('form')
     return render(request,'form.html')

def delete_data(request,id):
     data=Student.objects.get(id=id)
     data.isdelete=True
     data.save()
     #data.delete()
     return redirect('home')


def recycle_bin(request):
    data = Student.objects.filter(isdelete=True)
    return render(request, 'recycle_bin.html', {'data': data})

def restore_data(request,id):
     data=Student.objects.get(id=id)
     data.isdelete=False
     data.save()
     #data.delete()
     return redirect('home')

def edit(request,id):
    data=Student.objects.get(id=id)
    if request.method=="POST":
          data=(request.POST)
          n=data['name']
          a=data['age']
          e=data['email']
          ad=data['address']
           
         # var= Student(name=n,contact=c,email=e,message=m)
          data=Student.objects.get(id=id)
          data.name=n
          data.age=a
          data.email=e
          data.address=ad
          data.save()
          return redirect('home')
    
    return render(request,'edit.html',{'data':data})
