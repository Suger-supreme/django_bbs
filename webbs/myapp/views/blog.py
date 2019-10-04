from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from myapp import forms
from  myapp import models
from django.db.models import Count

import logging
# 生成一个logger实例，专门用来记录日志
logger = logging.getLogger(__name__)
print(logger,"日志对象哈哈哈")



def homes(request,arg):
    print(arg)
    # 去UserInfo表里把用户对象取出来
    user = models.UserInfo.objects.filter(username=arg).first()
    if not user:
        return HttpResponse("404")
    # 如果用户存在需要将TA写的所有文章找出来
    blog = user.blog
    print(blog,"111111111111111111111111")
    # 我的文章列表
    article_list = models.Article.objects.filter(user=user)
    print(article_list,"222222222222222222222222222222222")


    # 我的文章分类及每个分类下文章数
    # 将我的文章按照我的分类分组，并统计出每个分类下面的文章数
    # category_list = models.Category.objects.filter(blog=blog)
    # category_list=models.Category.objects.filter(blog=blog)
    # print(category_list,"333333333333333333333333333333333")
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # [{'title': '技术', 'c': 2}, {'title': '生活', 'c': 1}, {'title': 'LOL', 'c': 1}]
    # QuerySet[{'title': '技术类', 'c': 0}, {'title': '物理类', 'c': 0}] >
    print(category_list,"33333333333333333333333")
    # 统计当前站点下有哪一些标签，并且按标签统计出文章数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    print(tag_list,"44444444444444444444444444444")
    # 按日期归档
    #
    # aa = models.Article.objects.filter(user=user).extra(
    #         select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    #     ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")
    # print(aa)

    # return HttpResponse("11111")
    return  render(request,"03blog/01homes.html",{"blog":blog,"article_list":article_list,"category_list":category_list,"tag_list":tag_list})






# 封装
# def get_left_menu(username):
#     user = models.UserInfo.objects.filter(username=username).first()
#     blog = user.blog
#     category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
#     tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
#     # 按日期归档
#     archive_list = models.Article.objects.filter(user=user).extra(
#         select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
#     ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")
#
#     return category_list, tag_list, archive_list




def arti_aa(request,username,pk):
    """
    :param username: 被访问的blog的用户名
    :param pk: 访问的文章的主键id值
    :return:
    """
    user = models.UserInfo.objects.filter(username=username).first()
    if not user:
        return HttpResponse("404")
    blog = user.blog
              # 找到当前的文章
    article_obj = models.Article.objects.filter(pk=pk).first()


    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # [{'title': '技术', 'c': 2}, {'title': '生活', 'c': 1}, {'title': 'LOL', 'c': 1}]
    # QuerySet[{'title': '技术类', 'c': 0}, {'title': '物理类', 'c': 0}] >


    # 统计当前站点下有哪一些标签，并且按标签统计出文章数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")

    # 所有评论列表
    comment_list = models.Comment.objects.filter(article_id=pk)

    return render(request,"03blog/02article.html",{"username":username,"article": article_obj,"blog":blog," category_list":category_list,"tag_list":tag_list,"comment_list":comment_list})







# 赞
import json
from django.db.models import F

def up_down(request):
    print(request.POST)
    article_id = request.POST.get('article_id')
    is_up = json.loads(request.POST.get('is_up'))
    user=request.user

    response = {"state": True}
    print("is_up", is_up)
    try:
        models.ArticleUpDown.objects.create(user=user, article_id=article_id, is_up=is_up)
        models.Article.objects.filter(pk=article_id).update(up_count=F("up_count") + 1)
    except Exception as e:
        response["state"] = False
        aa=models.ArticleUpDown.objects.filter(user=user, article_id=article_id).first().is_up
        print(aa,"2222222233333333333332222")
        response["fisrt_action"] = models.ArticleUpDown.objects.filter(user=user, article_id=article_id).first().is_up

    return JsonResponse(response)
    # return HttpResponse(json.dumps(response))









# 评论
def comment(request):
      print(request.POST)
      pid = request.POST.get("pid")
      article_id = request.POST.get("article_id")
      content = request.POST.get("content")
      user_pk = request.user.pk
      print(user_pk,"3333333333333333333333333333333333333333333333")

      response = {}
      if not pid:  # 根评论
          comment_obj = models.Comment.objects.create(article_id=article_id, user_id=user_pk, content=content)
      else:
          comment_obj = models.Comment.objects.create(article_id=article_id, user_id=user_pk, content=content,
                                                      parent_comment_id=pid)

      response["create_time"] = comment_obj.create_time.strftime("%Y-%m-%d")
      response["content"] = comment_obj.content
      response["username"] = comment_obj.user.username
      return JsonResponse(response)



# 子评论  评论树
def comment_tree(request,article_id):
    ret=list(models.Comment.objects.filter(article_id=article_id).values("pk","content","parent_comment_id"))
    print(ret,"666666666666")
    return JsonResponse(ret,safe=False)   # 非字典必须加safe=False






# 编辑器  添加文章
# https://www.cnblogs.com/52forjie/p/7913053.html     from bs4 import BeautifulSoup
# Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。
#
# Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。

def add_article(request):
    if request.method == "POST":
        title = request.POST.get('title')
        article_content = request.POST.get('article_content')
        user = request.user


        from bs4 import BeautifulSoup
        bs = BeautifulSoup(article_content, "html.parser")
        desc = bs.text[0:150] + "..."
        # 过滤非法标签xss攻击
        for tag in bs.find_all():
            print(tag.name)
            if tag.name in ["script", "link"]:
                tag.decompose()
        article_obj = models.Article.objects.create(user=user, title=title, desc=desc)
        models.ArticleDetail.objects.create(content=str(bs), article=article_obj)
        return redirect("/index/")
    return render(request,"04addhtml/01add_article.html")
























# 上传图片

import os,json
from  webbs import  settings
def add_upload(request):
    print(request.FILES)
    obj = request.FILES.get("upload_img")
    print("name",obj.name)
    path=os.path.join(settings.MEDIA_ROOT,"add_img",obj.name)
    print(path,"sssssssssssss")

    with open(path,"wb") as f:
        for line in obj:
            f.write(line)

    res={
        "error":0,
        "url":"/media/add_img/"+obj.name
    }

    return HttpResponse(json.dumps(res))

