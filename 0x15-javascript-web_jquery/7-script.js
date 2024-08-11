/* global $ */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json', // The URL to fetch data from
  method: 'GET', // The HTTP method to use (GET, POST, etc.)
  dataType: 'json', // Expected data type of the response
  success: function (response) {
    $('DIV#character').text(response.name);
  },
  error: function (xhr, status, error) {
    // Handle errors here
    console.error('Error occurred:', status, error);
  }
});
