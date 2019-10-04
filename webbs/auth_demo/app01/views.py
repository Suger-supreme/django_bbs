from django.shortcuts import render, redirect
from app01 import models
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        user = models.UserInfo.objects.filter(name=username, password=pwd).first()
        if user:
            # 登陆成功
            request.session["user_id"] = user.id
            return redirect("/index/")

    return render(request, "login.html")


def index(request):
    user_id = request.session.get("user_id")
    user_obj = models.UserInfo.objects.filter(id=user_id).first()

    return render(request, "index.html", {"obj": user_obj})


def home(request):
    print("这是在视图：home")
    print(request.user)
    user_id = request.session.get("user_id")
    user_obj = models.UserInfo.objects.filter(id=user_id).first()
    return render(request, "home.html")