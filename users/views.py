from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']

        print(f"DEBUG: Отримано phone={phone}, password={password}")

        user = authenticate(request, username=phone, password=password)
        print(f"DEBUG: Результат authenticate={user}")

        if user:
            login(request, user)
            return redirect('/students/')
        else:
            print("DEBUG: Користувача не знайдено або пароль невірний")

    return render(request, 'users/login.html')