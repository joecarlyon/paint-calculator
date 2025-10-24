$(document).ready(function() {
    function insertPaintCalculations() {
        var dimensionData = $('#dimensions').text();
        var endpoint = '/api/v1/calculate';

        if (!dimensionData) {
            console.error('No dimension data found');
            return;
        }

        try {
            var parsedData = JSON.parse(dimensionData);

            // Transform the data to match API expectations
            var transformedData = {};
            $.each(parsedData, function(roomKey, roomData) {
                transformedData[roomKey] = {
                    length: roomData.length,
                    width: roomData.width,
                    height: roomData.height
                };
            });

            $.ajax(endpoint, {
                data: JSON.stringify(transformedData),
                contentType: 'application/json',
                type: 'POST',
                success: function(data) {
                    $.each(data, function(roomName, val) {
                        if (roomName == 'total_gallons') {
                            $("#sumGallons").text('Total Gallons Required: ' + val);
                        } else {
                            var tds = $('#' + roomName).find('td');
                            tds.eq(0).text(val['room']);
                            tds.eq(1).text(val['ft']);
                            tds.eq(2).text(val['gallons']);
                        }
                    });
                },
                error: function(xhr, status, error) {
                    console.error('AJAX error:', xhr.responseText);
                }
            });
        } catch (e) {
            console.error('Error parsing dimension data:', e);
        }
    }

    setTimeout(insertPaintCalculations, 5000)
});