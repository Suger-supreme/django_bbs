from django.conf.urls import url,include
from django.contrib import admin
from myapp.views  import  Verify_reg_login
from home import index_show
from myapp.views  import home
from django.conf import settings
from django.views.static import serve

from myapp.views  import blog
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_show.index_show),




    url(r'^login/', Verify_reg_login.login),
    url(r'^reg/', Verify_reg_login.register),
    url(r'^logout/', Verify_reg_login.logout),
    # # 极验滑动验证码 获取验证码的url
    url(r'^pc-geetest/register', Verify_reg_login.get_geetest),
    # 专门用来校验用户名是否已被注册的接口
    url(r'^check_username_exist/$', Verify_reg_login.check_username_exist),



    url(r'^index/', home.index),

    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),


    # 将所有以blog开头的url都交给myapp下面的urls.py来处理
    url(r'^blog/', include('myapp.blog_urls')),

    url(r'^add_upload/',blog.add_upload ),

]

