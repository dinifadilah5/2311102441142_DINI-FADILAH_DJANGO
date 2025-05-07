from django.shortcuts import render

def home(request):
    template_name = ('halaman/index.html')
    context = {}
    return render(request, template_name, context)

def blog(request):
    template_name = ('halaman/blog-stl.html')
    context = {}
    return render(request, template_name, context)

def contact(request):
    template_name = ('halaman/contact-stl.html')
    context = {}
    return render(request, template_name, context)

