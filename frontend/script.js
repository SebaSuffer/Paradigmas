const ctx = document.getElementById('myChart');
datos=[];
url="http://127.0.0.1:5000/estadisticos";
$.ajax({
    contentType: "application/json",
    type: "GET",
    url:url,
})
.done(function( data, textStatus, jqXHR ) {
   //console.log();
   datos=data;
   new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Manhattan', 'Brooklyn','Queens', 'Bronx', 'Staten Island'],
      datasets: [{
        label: 'Personas con tumor',
        data: [data[0]["Manhattan"], data[0]["Brooklyn"],data[0]["Queens"],data[0]["Bronx"],data[0]["Staten Island"]],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});
