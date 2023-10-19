from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import movie


# Create your views here.
def index(request):
    mov=movie.objects.all()
    dict={'movie_list':mov}
    return render(request,'index.html',dict)
def detail(request,movie_id):
    m=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'mo':m})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year=request.POST.get('year')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        mov=movie(name=name,year=year,desc=desc,img=img)
        mov.save()
    return render(request,'add.html')
def update(request,id):
    mov=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':mov,'form':form})
def delete(request,id):
    if request.method=='POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')