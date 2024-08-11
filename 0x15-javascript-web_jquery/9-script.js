/* global $ */
$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr', // The URL to fetch data from
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
});
