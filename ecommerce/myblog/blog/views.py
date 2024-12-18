from django.shortcuts import render
from blog.models import Post

def home(request):
      posts = Post.objects.all()
      return render(request ,'pages/home.html', context)
def single(request, single):
      single = Post.objects.get(id=single)
      context = {
            'post':single
      }
      return render(request ,'pages/single.html', context)
