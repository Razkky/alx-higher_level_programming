$(function () {
    $.ajax ({
        type: "GET",
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        success: function (data) {
            let results = data.results;
            $.each(results, function (i, result) {
                $('#list_movies').append("<li>" + result.title + "</li>")
            })
        }
    });
});
