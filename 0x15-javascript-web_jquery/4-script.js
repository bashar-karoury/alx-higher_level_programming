/* global $ */
$('DIV#toggle_header').on('click', function () {
  if ($(this).hasClass('red')) {
    $(this).removeClass('red');
    $(this).addClass('green');
  } else {
    $(this).removeClass('green');
    $(this).addClass('red');
  }
});
