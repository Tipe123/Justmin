//we create a whole map view
    //we display a map with thid code
    const apiKey = 'So6Le40CQ5Ut3T2KlAGYLCVDiPl2SW9B';
    const map = tt.map({
        key: apiKey,
        container: 'map',
        center:[-0.12634, 51.50276],
        zoom: 1
    });

    //This are the controls of the map
    map.addControl(new tt.FullscreenControl());
    map.addControl(new tt.NavigationControl());

map.on('load', function() {

    map.showTrafficFlow();
    map.addLayer({
        'id': 'overlay',
        'type': 'fill',
        'source': {
            'type': 'geojson',
            'data': {
                'type': 'Feature',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [[[-0.2046175878910219, 51.52327158962092],
                        [-0.05355557617221507, 51.53523241868879],
                        [-0.13045987304786877, 51.46299250930767]]]
                }
            }
        },
        'layout': {},
        'paint': {
            'fill-color': '#db356c',
            'fill-opacity': 0.5,
            'fill-outline-color': 'black'
        }
    });
});

console.log(hey);