from django.shortcuts import render
from blog.models import Kategori, MyBlog

# Create your views here.
def home(request):
    template_name = ('base/index.html')
    context = {}
    return render(request, template_name, context)

def contact(request):
    template_name = ('base/contact-stl.html')
    context = {}
    return render(request, template_name, context)

def kategori_list(request):
    template_name = ('home/snippets/kategori_list.html')
    kategori = Kategori.objects.all()
    print(kategori)
    context = {
        'kategori': kategori,
    }
    return render(request, template_name, context)

def myblog(request):
    myblog_list = MyBlog.objects.all()
    template_name = ('base/blog-stl.html')
    context = {}
    return render(request, template_name, context)