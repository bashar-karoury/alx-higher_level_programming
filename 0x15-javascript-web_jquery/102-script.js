/* global $ */
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/';

  $('INPUT#btn_translate').on('click', function () {
    const inputValue = $('INPUT#language_code').val();
    if (inputValue) {
      const langUrl = `${url}?lang=${inputValue}`;
      console.log(langUrl);
      $.ajax({
        url: langUrl,
        method: 'GET', // The HTTP method to use (GET, POST, etc.)
        dataType: 'json', // Expected data type of the response
        success: function (response) {
          $('DIV#hello').text(response.hello);
        },
        error: function (xhr, status, error) {
          // Handle errors here
          console.error('Error occurred:', status, error);
        }
      });
    }
  });
});
