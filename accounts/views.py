from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile

# تسجيل حساب جديد
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم مستخدم بالفعل.')
            return redirect('register')

        if UserProfile.objects.filter(phone=phone).exists():
            messages.error(request, 'رقم الجوال مستخدم بالفعل.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, phone=phone)
        messages.success(request, 'تم التسجيل بنجاح. يمكنك الآن تسجيل الدخول.')
        return redirect('login')

    return render(request, 'accounts/register.html')

# تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح.')
            return redirect('home')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')

    return render(request, 'accounts/login.html')

# تسجيل الخروج
def logout_view(request):
    logout(request)
    return redirect('home')
