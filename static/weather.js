var userLat;
var userLng;
// gets user's current latitude and longitude
navigator.geolocation.watchPosition(function(position) {
    // Update user's latitude and longitude
    console.log(position);
    userLat = position.coords.latitude;
    userLng = position.coords.longitude;
});

function showWeatherResults(data) {

    console.log(data);

    var temp = data.temp;
    var humidity = data.humidity;
    var wind = data.wind;
    var overall = data.overall;

    var info = "TEMP IS " + temp +
            " HUMIDITY IS " + humidity +
            " IT IS THIS MUCH WINDY: " + wind +
            " overall it is " + overall;

    $('#weather').html(info);
}

$('#click').click(function(){
    $.post('/weather_results.json',
        {'userLat': userLat,
        'userLng': userLng}, showWeatherResults);
    }
);

