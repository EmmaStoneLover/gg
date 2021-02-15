
input_vue = new Vue({
	el: "#msg_title_and_input",
	delimiters: ['[[', ']]'],
	data: {
    msg_input: true,
    msg_input_adds: true,
		vue_text: '',
		user_check: document.getElementById('user_name').name,
		vue_user: document.getElementById('user_name').name,
		vue_card_bg_color_choice: 'bg-dark',
		vue_card_font_color_choice: 'text-white',
	},
	beforeMount(){
	 this.user_check == 'Войти' ? this.vue_user = '' : this.vue_user = this.user_check
	},
});

var reader = new FileReader();
reader.onload = function (e) {
	var output = document.getElementById("input_image");
	output.innerHTML = "<img src='" + e.target.result + "' />";
};
function input_image_onchange(files) {
	var file = files[0];
	reader.readAsDataURL(file);
}

// --------------------------------------------------------- Поиск по Новостям --------
// msg_id = document.getElementsByClassName('msg_text');
// for (var i = msg_id.length - 1; i >= 0; i--) {
//   console.log(i)
  
// }

// msg_vue = new Vue({
//   el: "#msg_search_and_msgs",
//   delimiters: ['[[', ']]'],
//   data: {
    
//   },
  
// });


function msg_search_find() {
  $('p#msg_not_found').hide();
  $('div.msg_msgs').show();
  search = $("#msg_search_input").val();
  jQuery.expr[":"].Contains = jQuery.expr.createPseudo(function(arg) {
    return function( elem ) {
        return jQuery(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
  });
  search_fined = $('*:Contains('+search+')').closest("div.msg_msgs");
  if (search_fined.length) {
    $('div.msg_msgs').hide();
    search_fined.show();
  }
  else {
    $('p#msg_not_found').show();
    $('div.msg_msgs').hide();
  };
};
function msg_search_clear() {
  $('p#msg_not_found').hide();
  $('div.msg_msgs').show();
  $("#msg_search_input").val('');
};
$(document).keydown( function(e) {
  e.keyCode === 13 ? msg_search_find() : false
  e.keyCode === 27 ? msg_search_clear() : false
});
$('#msg_search_input_button_find').on('click', function() { msg_search_find() });
$('#msg_search_input_button_clear').on('click', function() { msg_search_clear() });
