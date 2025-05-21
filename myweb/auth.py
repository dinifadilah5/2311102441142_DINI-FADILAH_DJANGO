from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
def akun_login(request):
    #jika user sudah login, maka tidak boleh akses fungsi ini lagi
    if request.user.is_authenticated:
        return redirect('dashboard')

    template_name = 'halaman/login.html'
    pesan=''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            pesan = "Gagal Login"
    context = {
        'pesan': pesan
    }
    return render(request, template_name)

