from  myapp.views import blog
from django.conf.urls import url

urlpatterns = [
    # url(r'article/(\d+)/$',blog.arti_aa),  # 文章详情  article_detail(request, xiaohei, 1)

    url(r"add/",blog.add_article),


   # 评论
    url(r"comment/", blog.comment),

    # 评论树
     url(r"comment_tree/(\d+)/", blog.comment_tree),

   # 赞
    url(r"up_down/", blog.up_down),

    url(r'(\w+)/article/(\d+)/$', blog.arti_aa),  # 文章详情  article_detail(request, xiaohei, 1)

    url(r'(\w+)', blog.homes),     # home(request, username)


]

