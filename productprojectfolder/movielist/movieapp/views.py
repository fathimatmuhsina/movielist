from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movieform


# Create your views here.

def index(request):
    mov = movie.objects.all()
    context = {'movie_list': mov}
    return render(request,'index.html', context)
def detail(reuest,movie_id):
    mid =movie.objects.get(id=movie_id)
    return render(reuest,"detail.html",{'mid':mid})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']

        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()

    return render(request,'add.html')

def update(request,id):
    mov=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')
