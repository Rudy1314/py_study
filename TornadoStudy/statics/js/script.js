/**
 * Created by RU on 2017/9/3.
 */
$(document).ready(function () {
    $("#login").click(function () {
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username": user, "password": pwd};
        $.ajax({
            type: "post",
            url: "/",
            data: pd,
            cache: false,
            success: function (data) {
                console.log(data)
                window.location.href = "/user?user=" + data;
            },
            error: function () {
                alert("error!");
            },
        });
    });
});
