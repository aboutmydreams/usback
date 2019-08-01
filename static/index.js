window.onload = function () {
    function isWeixin() {
        var ua = navigator.userAgent.toLowerCase(); //获取判断用的对象
        if (ua.match(/MicroMessenger/i) == "micromessenger") {
            return true; //微信打开
        } else {
            return false; //不是微信打开
        }
    }

    document.getElementById("open_app").onclick = function (e) {
        if (isWeixin()) {
            var modPop = document.getElementById("mod_pop");
            modPop.style.display = "block";
        } else {

            if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
                //ios判断
                window.location.href = "usapp://"; //通过app打开协议来打开app
                window.setTimeout(function () {
                    window.location.href =
                        "https://itunes.apple.com/cn/app/id477927812"; //没有弹框打开app则打开app下载地址
                }, 20);
            } else if (/(Android)/i.test(navigator.userAgent)) {
                //Android判断
                var state = null;
                try {
                    state = window.open("usapp://");
                } catch (e) {
                }
                if (state) {
                    //window.close();
                } else {
                    window.location.href =
                        "https://www.baidu.com";
                }
            }else {
                window.location.href =
                        "https://www.baidu.com";
            }
        }
    };
};
