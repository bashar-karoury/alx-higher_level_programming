/* global $ */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json', // The URL to fetch data from
  method: 'GET', // The HTTP method to use (GET, POST, etc.)
  dataType: 'json', // Expected data type of the response
  success: function (response) {
    for (const movie of response.results) {
      // Create a new list item
      const newItem = $('<li>').text(movie.title);
      // Append the new item to the list
      $('UL#list_movies').append(newItem);
    }
  },
  error: function (xhr, status, error) {
    // Handle errors here
    console.error('Error occurred:', status, error);
  }
});
