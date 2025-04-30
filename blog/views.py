from django.shortcuts import render
from blog.models import Kategori, MyBlog

# Create your views here.
def home(request):
    template_name = ('halaman/index.html')
    context = {}
    return render(request, template_name, context)

def contact(request):
    template_name = ('dashboard/contact-stl.html')
    context = {}
    return render(request, template_name, context)


def kategori_list(request):
    template_name = ('halaman/snippets/kategori_list.html')
    kategori = Kategori.objects.all()
    print(kategori)
    context = {
        'kategori': kategori,
    }
    return render(request, template_name, context)

def myblog(request):
    myblog_list = MyBlog.objects.all()
    template_name = ('dashboard/blog-stl.html')
    context = {}
    return render(request, template_name, context)

