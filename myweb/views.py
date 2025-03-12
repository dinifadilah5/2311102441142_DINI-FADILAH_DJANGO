from django.shortcuts import render

def home(request):
    template_name = 'myweb/home.html'
    context = {
        'title': 'My Home Page',
        'welcome': 'Welcome Home'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'myweb/about.html'
    context = {
        'title': 'about me',
        'welcome': 'ini page about',
    }
    return render(request, template_name, context)