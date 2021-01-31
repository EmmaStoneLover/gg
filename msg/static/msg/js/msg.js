

var input = new Vue({
	el: "#app",
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
	methods: {
		vue_user_func: function() {
			if (this.user_check === 'Войти') {this.vue_user = ''}
			else {this.vue_user = this.user_check}
		}
	},
	beforeMount(){
	 this.vue_user_func()
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



// Поиск по Новостям

function msg_search_find() {
  $('p#msg_not_found').hide();
  $('div.msg_msgs').show();
  search = $("#msg_search_input").val();
  search_fined = $('*:contains('+search+')').closest("div.msg_msgs");
  if (search_fined.length > 0 ) {
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
  if (e.keyCode === 13) { msg_search_find() }
  if (e.keyCode === 27) { msg_search_clear() }
});
$('#msg_search_input_button_find').on('click', function() { msg_search_find() });
$('#msg_search_input_button_clear').on('click', function() { msg_search_clear() });
