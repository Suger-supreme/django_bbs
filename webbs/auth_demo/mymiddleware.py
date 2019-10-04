from django.utils.deprecation import MiddlewareMixin
from app01 import models

class MyAuth(MiddlewareMixin):
    """
    中间件有五种方法：
        process_request
        process_view
        process_exception
        process_template_response
        process_response
    """

    def process_request(self, request):
        print("一声叹息！！！")
        user_id = request.session.get("user_id")
        if user_id:
            # 登录的用户你要把request.user赋值为登陆的用户对象
            user_obj = models.UserInfo.objects.filter(id=user_id).first()
            request.user = user_obj
        else:
            # 没有登录的用户要把request.user赋值为匿名用户
            request.user = {"name": "", "password": ""}
