$(document).ready(function() {
    $('<div class="policyInfo policyTitle" id="policyTitle">Policy</div> <div class="policyInfo policyText" id="policyText"> </div>').insertAfter($('#formfield-form-widgets-message')[0])
        $.ajax({
            url : "/Plone/policy",
            dataType: "text",
            success : function (data) {
                $(".policyInfo.policyText").html($(data).find('#parent-fieldname-text').html());
            }
        });

});
