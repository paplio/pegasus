function initialize() {

var input = document.getElementById('destinationField');
//var options = { componentRestrictions: 
				//types: ['cities']
				//{country: "in"}
//			//
var autocomplete = new google.maps.places.Autocomplete(input);
}
google.maps.event.addDomListener(window, 'load', initialize);

