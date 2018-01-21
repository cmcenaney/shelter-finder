
console.log(window.appConfig)
function initMap() {
       var shelters = [
          {
            "name": "Domestic Violence Shelter - The Open Gate",
            "address": "2901 Market St, Wilmington, NC 28401, USA",
            "lat": 34.235848,
            "long": -77.943268,
            "url": "http://www.domesticviolence-wilm.org/"
          },
          {
            "name": "Shelter for Battered Women",
            "address": "600 E 5th St, Charlotte, NC 28202, USA",
            "lat": 35.22291,
            "long": -80.835917,
            "url": "http://www.domesticviolence-wilm.org/"
          },
          {
            "name": "Coastal Women's Shelter",
            "address": "1333 S Glenburnie Rd, New Bern, NC 28562, USA",
            "lat": 35.105613,
            "long": -77.099946,
            "url": "http://www.domesticviolence-wilm.org/"
          },
          {
            "name": "Onslow Women's Center Inc",
            "address": "226 New Bridge St, Jacksonville, NC 28540, USA",
            "lat": 34.749013,
            "long": -77.4196088,
            "url": "http://www.domesticviolence-wilm.org/"
          }
        ];

        var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: {{location.latitude}}, lng: {{location.longitude}}},
          zoom: 11
        });

        for (var i in shelters){
  
          var shelterCircle = new google.maps.Circle({
            strokeColor: '#FF0000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#FF0000',
            fillOpacity: 0.35,
            map: map,
            center: {lat: shelters[i].lat, lng: shelters[i].long},
            radius: 10
          });
        }


      }
