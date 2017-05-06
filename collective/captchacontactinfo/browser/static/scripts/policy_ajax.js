require([
  'jquery',
  'mockup-patterns-modal',
], function($, Modal) {
  'use strict';
   $(document).ready(function(){
     var myvet = $(location.pathname.split("/"))
     var mylocation = $(location.pathname.split("/"))[myvet.length-1]

     if (mylocation === 'contact-info'){
       render_policy()
     }
     else{
       $('ul li a[href$="contact-info"]').each(function() {
          var modal = new Modal($(this), {
          });
          modal.on('after-render', function(){
           render_policy()
          });
        });
     }
   });
 });


function render_policy(){
  portal_url = $('body').data('portalUrl')
  $('<div class="policyInfo policyTitle" id="policyTitle">Policy</div> <div class="policyInfo policyText" id="policyText"> </div>').insertAfter($('#formfield-form-widgets-message')[0])
  $.ajax({
      url: portal_url + '/get_policy_page_url',
      dataType: "text",
      success : function (data) {
          $(".policyInfo.policyText").html($(data));
      }
  });
}
