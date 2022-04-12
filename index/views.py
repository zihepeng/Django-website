import json
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from .models import movies, grade
from django.views.generic import View
# Create your views here.
def home(request):
        return render(request,'index/index.html')

def movies_select_all(request):
    movies_list = movies.objects.all()
    return render(request, 'index/movies.html', {'movies_list': movies_list})

def movies_delete(request):
    sid = request.GET.get('sid')
    movie = movies.objects.get(id=sid)
    movie.delete()
    return redirect(reverse('index:movies_select_all'))

def movies_insert(request):
    grade_list = grade.objects.all()
    return render(request, 'index/movie_insert.html', {'grade_list': grade_list})

def movies_insert_handler(request):

    mname = request.POST.get('mname')
    mduration = request.POST.get('mduration')
    mimg = request.POST.get('mimg')
    mticket = request.POST.get('mticket')
    mgradetype_id = request.POST.get('mgradetype_id')

    movie=movies()
    movie.mname=mname
    movie.mduration=mduration
    movie.mimg=mimg
    movie.mticket = mticket
    movie.mgradetype_id=mgradetype_id
    movie.save()
    return redirect(reverse('index:movies_select_all'))


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = 'please insert key word'
        return render(request, 'index/movies.html', {'error_msg': error_msg})

    post_list = movies.objects.filter(mname__icontains=q)
    return render(request, 'index/results.html', {'error_msg': error_msg,
                                                'post_list': post_list})
