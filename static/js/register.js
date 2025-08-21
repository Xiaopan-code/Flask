// 定义成一个函数
function bindEmailCpatchaClick(){
        $("#captcha-btn").click(function(event){
        // $this 代表的是当前按钮的jquery对象
        var $this = $(this);
        // 阻止默认的事件
        event.preventDefault();
        // 获取输入的邮箱 以便后续操作
        var email = $("input[name='email']").val();

        // 新版jQuery可以省略method，直接用type
        // 也可以使用更简洁的$.get()方法
        $.get("/auth/captcha/email", {email: email})
            .done(function(result){
                // 如果验证码发送成功则开始倒计时
                if(result.code === 200){
                    // 倒计时事件为60s
                    var countdown = 60;
                    // 开始倒计时之前取消按钮点击事件
                    $this.off("click");
                    // 定义定时器对象，返回一个对象
                    var timer = setInterval(function (){
                        $this.text(countdown);
                        countdown -= 1;
                        if(countdown <= 0){
                            // 如果倒计时<=0 就清掉定时器
                            clearInterval(timer);
                            // 将按钮显示内容回调
                            $this.text("获取验证码");
                            // 重新执行函数去绑定点击事件
                            bindEmailCpatchaClick
                        }
                    }, 1000);
                    alert("邮箱验证码发送成功");
                }else{
                    // 处理服务器明确告诉客户端业务失败
                    alert(result.message);
                }
            })
            // 处理请求过程本身出错
            .fail(function(error){
                console.log("请求失败:", error);
                alert("获取验证码失败，请稍后重试");
            });
    });
}

// 整个网页都加载后再去执行函数
$(function (){
    bindEmailCpatchaClick();
});
