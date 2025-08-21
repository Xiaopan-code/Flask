// 整个网页都加载后再去执行函数
$(function (){
    $("#captcha-btn").click(function(event){
        // 阻止默认的事件
        event.preventDefault();

        var email = $("input[name='email']").val();

        // 新版jQuery可以省略method，直接用type
        // 也可以使用更简洁的$.get()方法
        $.get("/auth/captcha/email", {email: email})
            .done(function(result){
                if(result.code === 200){
                    alert("邮箱验证码发送成功");
                }else{
                    alert(result.message);
                }
            })
            .fail(function(error){
                console.log("请求失败:", error);
                alert("获取验证码失败，请稍后重试");
            });
    });
});
