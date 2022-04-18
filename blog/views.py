from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .models import Blogpost
# Create your views here.

def index(request):
    myposts= Blogpost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html', {'myposts': myposts})

    
def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html',
                  {'post':post})

def contact(request):
    return render(request,'blog/contact.html')

def about(request):
    return render(request,'blog/about.html')