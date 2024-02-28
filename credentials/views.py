from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.messages import info
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm




# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('credentials:film')

        else:
            messages.info(request, "invalid credentials")
            return redirect('credentials:login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)

                user.save();
            return redirect('credentials:login')


        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def film(request):
    movie = Movie.objects.all()
    context ={
       'movie_list': movie
    }
    return render(request, "film.html", context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        actors = request.POST.get('actors', )
        category = request.POST.get('category', )
        link = request.POST.get('link', )
        rate = request.POST.get('rate',)
        review = request.POST.get('review', )
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, actors=actors, category=category, link=link,rate=rate,review=review, img=img)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')









