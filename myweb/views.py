from django.shortcuts import render

def home(request):
    template_name = ('halaman/index.html')
    context = {}
    return render(request, template_name, context)

def contact(request):
    template_name = ('dashboard/contact-stl.html')
    context = {}
    return render(request, template_name, context)

def myblog(request):
    template_name = ('dashboard/blog-stl.html')
    context = {}
    return render(request, template_name, context)