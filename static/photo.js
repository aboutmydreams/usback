function validateForm() {
    var x = document.forms["myForm"]["username"].value;
    var y = document.forms["myForm"]["password"].value;
    if (x == null || x == "") {
        alert("请上传图片哟");
        return false;
    }
    // if (y == null || y == "") {
    //     alert("需要输入联系电话哟");
    //     return false;
    // }
    // if (x.length>4) {
    //     alert("正确输入姓名哟");
    //     return false;
    // }
    // if (y.length!=11) {
    //     alert("正确输入联系电话哟");
    //     return false;
    // }
}