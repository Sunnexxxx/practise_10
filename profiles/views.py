from django.shortcuts import render, redirect
from .models import UserProfile


def profiles_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profiles_list.html', {'profiles': profiles})


def register_profile(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        username = request.POST.get('username')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobbies = request.POST.get('hobbies')
        favorite_music = request.POST.get('favorite_music')
        city = request.POST.get('city')
        favorite_food = request.POST.get('favorite_food')
        login = request.POST.get('login')
        try:
            UserProfile.objects.create(
                nickname=nickname,
                username=username,
                password=password,
                age=age,
                hobbies=hobbies,
                favorite_music=favorite_music,
                surname=surname,
                login=login,
                gender=gender,
                city=city,
                favorite_food=favorite_food
            )
            return redirect('profiles_list')
        except:
            error_message = 'Данный никнейм уже используется'
            return render(request, 'register_profile.html', {'error_message': error_message})

    return render(request, 'register_profile.html')


def user_profile(request, nickname):
    profile = UserProfile.objects.get(nickname=nickname)
    return render(request, 'user_profile.html', {'profile': profile})





