from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
import requests


# view to handle user login

def memes_login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("Current user credentails : ", username, password)

        current_user = authenticate(request, username=username, password=password)

        if current_user is None:
            print("Invalid user details")
            return render(request, "memesapp/login.html")
        else:
            print("Valid user details")
            login(request, current_user)

            return redirect("/displaymemes/")


    return render(request, "memesapp/login.html")



#view to display memes to user post login

def memes_displaymemes_view(request):
    url = 'https://api.imgflip.com/get_memes'

    r = requests.get(url)

    memes_data = requests.get(url).json()

    allmemes = []

    for i in range(0, 5):
        allmemes.append(memes_data['data']['memes'][i])

    return render(request, "memesapp/displaymemes.html", {'allmemes':allmemes})


#view to logout user

def memes_logout_view(request):

    logout(request)

    return render(request, "memesapp/login.html")









