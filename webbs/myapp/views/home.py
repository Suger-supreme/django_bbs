from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from myapp import forms
from  myapp import models

# https://www.cnblogs.com/liwenzhou/p/8660826.html
def index(request):

    article_list=models.Article.objects.all()
    return render(request,"02html/01home.html",{"article_list":article_list})
