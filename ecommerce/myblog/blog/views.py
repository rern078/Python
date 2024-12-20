from django.shortcuts import render
from blog.models import Post, Category
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

def home(request):
      post_list = Post.objects.all()
      paginator = Paginator(post_list, 1)

      page = request.GET.get('page')
      categories = Category.list_categories()

      try:
            posts = paginator.page(page)
      except PageNotAnInteger:
            posts = paginator.page(1)
      except EmptyPage:
            posts = paginator.page(paginator.num_pages)

      return render(request ,'pages/home.html', {'posts':posts, 'categories':categories})
def single(request, single):
      single = Post.objects.get(id=single)
      context = {
            'post':single
      }
      return render(request ,'pages/single.html', context)

def archive(request, category):
      cat = Category.objects.get(slug=category)
      post_list = Post.objects.filter(category__pk=cat.id)
      paginator = Paginator(post_list, 1)

      page = request.GET.get('page')
      categories = Category.list_categories()

      try:
            posts = paginator.page(page)
      except PageNotAnInteger:
            posts = paginator.page(1)
      except EmptyPage:
            posts = paginator.page(paginator.num_pages)

      return render(request ,'pages/archive.html', {'posts':posts, 'categories':categories, 'category':cat.title})