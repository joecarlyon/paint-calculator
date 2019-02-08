$( document ).ready(function() {
    function insertPaintCalculations() {
        var dimensionData = $('#dimensions').text();
        var endpoint = '/api/v1/calculate'
        $.ajax(endpoint, {
            data : dimensionData,
            contentType : 'application/json',
            type : 'POST',
            success: function ( data ) {
                $.each( data, function( roomName, val ) {
                        if (roomName == 'total_gallons') {
                            $("#sumGallons").append(val);
                        } else {
                            var tds = $('#' + roomName).find('td');
                            tds.eq(0).text(val['room']);
                            tds.eq(1).text(val['ft']);
                            tds.eq(2).text(val['gallons']);
                        }
                    });
                }
        });
    }
    setTimeout(insertPaintCalculations, 5000)
});