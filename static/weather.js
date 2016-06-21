
// gets user's current latitude and longitude
navigator.geolocation.watchPosition(function(position) {
    // Update user's latitude and longitude
    console.log(position);
    userLat = position.coords.latitude;
    userLng = position.coords.longitude;
});

// function showWeatherResults(data) {
//     $.get('/results')
// }

// $(document).ready(function(){
//     $.post('/',
//         {'userLat': userLat,
//         'userLng': userLng}, showWeatherResults);
//     }
// );