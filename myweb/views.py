from django.shortcuts import render

def home(request):
    template_name = 'portfolio/home.html'
    context = {
        'subtitle': 'Dini Fadillah',
        'body': 'Halaman Utama'
    }
    return render(request, template_name, context)