require(["jquery", "mockup-patterns-modal"], function ($, Modal) {
  "use strict";
  $(document).ready(function () {
    var myvet = $(location.pathname.split("/"));
    var mylocation = $(location.pathname.split("/"))[myvet.length - 1];

    if (mylocation === "contact-info") {
      render_policy();
    }
    // disabled because in RER they don't want it anymore
    //  else{
    //    $('a[href$="contact-info"]').each(function() {
    //       var modal = new Modal($(this), {
    //       });
    //       modal.on('after-render', function(){
    //        render_policy()
    //       });
    //     });
    //  }
  });
});

function render_policy() {
  portal_url = $("body").data("portalUrl");
  $.ajax({
    url: portal_url + "/get_policy_page_url",
    dataType: "text",
    success: function (data) {
      if (data) {
        $(
          '<div class="policyInfo policyTitle" id="policyTitle">Informativa privacy</div> <div class="policyInfo policyText" id="policyText"> </div>'
        ).insertAfter($("#formfield-form-widgets-message")[0]);
        $(".policyInfo.policyText").html($(data));
      }
    },
  });
}
