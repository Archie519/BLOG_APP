from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .import models 
from django.contrib.auth.decorators import login_required


# Create your views here.
def test(request):
    return render(request,'blog/base.html')


def index(request):
    return render(request, 'blog/index.html')





def login_view(request):
    if request.method == 'POST':
        name  = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request,userr)
            return redirect('/home')
        else:
            return redirect('/login')
    return render(request,'blog/login.html')




def signup(request):
    if request.method =='POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser=User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/login')
    return render(request,'blog/signup.html')





def home(request):
    context={
        'posts':Posts.objects.all()
    }
    return render(request,'blog/home.html',context)



def newpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Posts(title=title, content=content , author=request.user)
        npost.save()
        return redirect('/home')
    return render(request,'blog/newpost.html')
   



def mypost(request):
    context = {'posts':Posts.objects.filter(author = request.user)}
    return render(request,'blog/mypost.html',context)
    


def signout(request):
    logout(request)
    return redirect('/login')


def update_blog(request, blog_id):
    post = get_object_or_404(Posts, id=blog_id, author=request.user)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('/home')
    return render(request, 'blog/update_blog.html', {'blog': post})



def delete_blog(request, blog_id):
    post = get_object_or_404(Posts, id=blog_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('/home')
    return render(request, 'blog/delete_blog.html', {'blog': post})





