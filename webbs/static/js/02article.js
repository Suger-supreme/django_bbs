
$("#div_digg .action").click(function () {
    if ($(".info").attr("username")) {

          // 点赞或踩灭
          var is_up = $(this).hasClass("diggit");// {#绑定双事件时(#div_digg .action)  如果hasclass有disggit 返回true 没有返回fasle#}
          // var article_id="{{ article.pk }}";    // {#获取文章id(pk 主键)#}    使用静态文件独引入 这个{{}}是渲染不出来  但是有解决方法
          var article_id = $(".info").attr("article_id"); //这是上面{{}} 解决方法
          console.log(article_id, "2222222");


          $.ajax({
              url: "/blog/up_down/",
              type: "post",
              data: {
                  is_up: is_up,
                  article_id: article_id,
                  csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
              }, success: function (data) {
                  console.log(data);

                  if (data.state) {// 赞或者灭成功

                      if (is_up) {
                          var val = $("#digg_count").text();
                          val = parseInt(val) + 1;    //parseInt() 函数可解析一个字符串，并返回一个整数。
                          $("#digg_count").text(val);

                      } else {
                          var val = $("#bury_count").text();
                          val = parseInt(val) + 1;
                          $("#bury_count").text(val);

                      }

                  } else {
                      // 重复提交
                      if (data.fisrt_action) {
                          $("#digg_tips").html("您已经推荐过");
                      } else {
                          $("#digg_tips").html("您已经反对过");
                      }
                      setTimeout(function () {
                          $("#digg_tips").html("")
                      }, 1000);
                  }
              }
          });
      }else {
            location.href = "/login/"
      }
});


