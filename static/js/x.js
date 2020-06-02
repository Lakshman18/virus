var x = "{{country_stats.confirmed|safe}}";
var y ="{{country_stats.recovered|safe}}";
var z ="{{country_stats.deaths|safe}}";

var myConfig = {
  "type": "pie",
  "labels": [{
      "text": "How to prevent coronavirus disease infection?",
      "font-family": "Arial",
      "font-size": "15",
      "x": "60%",
      "y": "20%",
	  
	  "mediaRules": [
 	  {//changes layout at 800 pixels or less
 	    "maxWidth": 800,
 	    "x": '15%',
 	    "y": '65%',
 	     "font-size": "12",
 	    
 	  }]
    },
	
    {
      "text": "STAY HOME.SAVE LIVES.",
      "font-color": "red",
      "font-family": "Georgia",
      "font-size": "30",
      "x": "60%",
      "y": "26%",
	  
	   "mediaRules": [
 	  {//changes layout at 800 pixels or less
 	    "maxWidth": 800,
 	    "x": '15%',
 	    "y": '71%',
 	    "font-size": "20",
 	    
 	  }]
    },
    {
      "text": "(Click the above link.)",
      "font-family": "Georgia",
      "font-size": "10",
      "x": "60%",
      "y": "41%",
	  
	  "mediaRules": [
 	  {//changes layout at 800 pixels or less
 	    "maxWidth": 800,
 	    "x": '15%',
 	    "y": '78%',
 	    "font-size": "8",
 	    
 	  }]
    }
 	 
  ],
  "plot": {
    "value-box": {
      "placement": "out",
      "offset-r": "-10",
      "font-family": "Georgia",
      "font-size": 12,
      "font-weight": "normal"
	  
    }
  },
  "plotarea": {
    "margin-right": "45%",
    "margin-top": "0%",
    "margin-bottom": "20%",
	
	 "mediaRules": [
 	  {//changes layout at 800 pixels or less
	  "maxWidth": 800,
 	    "margin-right": "15%",
		"margin-left": "15%",
    "margin-top": "0%",
    "margin-bottom": "30%",
 	    
 	  }]
  },
  
  
  "series": [{
      "values": [parseInt(x)]
    },
    {
      "values": [parseInt(y)]
    },
    {
      "values": [parseInt(z)]
    }
  ]
};

zingchart.render({
  id: 'myChart',
  data: myConfig,
  height: 400,
  width: "100%"
});
$(function() {
  $("#resizable").resizable();
});