// delimiters: ['[[', ']]'],


var input = new Vue({
	el: "#msg_title_and_input",
	data: {
    msg_input: true,
    msg_input_adds: true
	},
	
});


user = $('#user_name').attr('name');
console.log(user);
if (user == "Войти") { $('#msg_input_user_hide').show() }
else { $('#msg_input_user').val(user) };

// $('p#msg_not_found').hide()
// $('#msg_input_add_hide').on('click', function() {
//   $('#msg_input_add_hide_div').toggleClass('invisible position-absolute z-index-property');
// });

remove_class_bg_list =
('bg-dark bg-white bg-light bg-primary bg-secondary bg-success bg-danger bg-warning bg-info');
remove_class_bg = function(){ return remove_class_bg_list };

remove_class_text_list =
('text-dark text-white text-primary text-secondary text-success text-danger text-warning text-info text-muted');
remove_class_text = function(){ return remove_class_text_list };

remove_class_btn_list =
('btn-dark btn-white btn-primary btn-secondary btn-success btn-danger btn-warning btn-info btn-muted');
remove_class_btn = function(){ return remove_class_btn_list };

inputs_bg = $('.msg_input_text_and_bg_color');


$('#id_card_bg_color_choice').change( function () {

  addclass = $('#id_card_bg_color_choice').val();

  $("#msg_input").removeClass( remove_class_bg );
  $("#msg_input").addClass( addclass );


  if ( addclass == 'bg-dark' ) {
    inputs_bg.removeClass( remove_class_bg + remove_class_text );
    inputs_bg.addClass('bg-dark text-white');
    $('#id_card_font_color_choice option').removeAttr('selected');
    $('#id_card_font_color_choice option[value=text-white]').attr('selected', 'selected');
    $("#msg_input").removeClass( remove_class_text );
    $("#msg_input_button").removeClass( remove_class_btn );
    $("#msg_input_button").addClass('btn-success');
  }

  if ( addclass == 'bg-warning' || addclass == 'bg-light') {
    inputs_bg.removeClass( remove_class_bg );
    inputs_bg.removeClass( remove_class_text );
    $('#id_card_font_color_choice option').removeAttr('selected');
    $('#id_card_font_color_choice option[value=text-dark]').attr('selected', 'selected');
    $("#msg_input").removeClass( remove_class_text );
    $("#msg_input").addClass('text-dark');
    $("#msg_input_button").removeClass( remove_class_btn );
    if ( addclass == 'bg-warning' ) {
      inputs_bg.addClass('bg-warning');
      $("#msg_input_button").addClass('btn-danger');
    }
    if ( addclass == 'bg-light' ) {
      inputs_bg.addClass('bg-light');
      $("#msg_input_button").addClass('btn-dark');
    }
  }

  if (addclass == 'bg-primary' ||
      addclass == 'bg-secondary' ||
      addclass == 'bg-success' ||
      addclass == 'bg-danger' ||
      addclass == 'bg-info'
    ) {
    inputs_bg.removeClass( remove_class_bg  );
    inputs_bg.removeClass( remove_class_text );
    $('#id_card_font_color_choice option').removeAttr('selected');
    $('#id_card_font_color_choice option[value=text-white]').attr('selected', 'selected');
    $("#msg_input").removeClass( remove_class_text );
    $("#msg_input_button").removeClass( remove_class_btn );
    if ( addclass == 'bg-success' ) {
      inputs_bg.addClass('bg-success text-white');
      $("#msg_input_button").addClass('btn-warning');
    }
    if ( addclass == 'bg-danger' ) {
        inputs_bg.addClass('bg-danger text-white');
      $("#msg_input_button").addClass('btn-info');
    }
    if ( addclass == 'bg-primary' ) {
      inputs_bg.addClass('bg-primary text-white');
      $("#msg_input_button").addClass('btn-danger');
    }
    if ( addclass == 'bg-secondary' ) {
      inputs_bg.addClass('bg-secondary text-white');
      $("#msg_input_button").addClass('btn-success');
    }
    if ( addclass == 'bg-info' ) {
      inputs_bg.addClass('bg-info text-white');
      $("#msg_input_button").addClass('btn-danger');
    }
  }

});

$('#id_card_font_color_choice').change( function () {
  addclass = $('#id_card_font_color_choice').val();
  $("#msg_input").removeClass( remove_class_text );
  $("#msg_input").addClass( addclass );
});

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
