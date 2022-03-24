$(document).ready(function() {
    $("#submit_user_message").click(function() {
        var user_message = $("#user_message").val();
        var query_string = '?question=' + user_message;
        window.location.href = "/" + query_string;
    });
});