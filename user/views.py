from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from user.models import User 
# Create your views here.



def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:     
                login(request, user)              
                return redirect('home')               
            else:
                messages.error(request, "Vous etez pas encore client")
                return render(request, 'user/login.html', {})
        else:
            return render(request, 'user/login.html', {})

    else:
        return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request): 
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        first_name = request.POST['first_name']
        print(first_name)
        last_name = request.POST['last_name']
        print(last_name)
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        age = int(request.POST['age'])
        phone = request.POST['phone']
        address = request.POST['address']
        image = request.POST['image']
        date_of_birth = request.POST['date_of_birth']
        place_of_birth = request.POST['place_of_birth']
        sexe = request.POST['sexe']
        print(password)
        user = User(username=username, first_name=first_name, last_name=last_name, email=email,
          password=password, age=age, phone=phone, address=address, image=image, date_of_birth=date_of_birth, place_of_birth=place_of_birth, sexe=sexe)
        print(user)
        user.save()
        print('Valideeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')      
        return render(request, 'user/register.html', {'user': user})
    else:
        print('non validesssssssssssssssssssssssssssssssssssssssssssssssssss')
        return render(request, 'user/register.html', )


