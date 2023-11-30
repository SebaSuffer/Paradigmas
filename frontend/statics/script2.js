$(document).ready(function () {
    // Función para obtener los datos y mostrar el gráfico
    $("#boton1").click(function () {
        $.get("/datos", function (data) {
            console.log("Datos obtenidos:", data);
            mostrarGrafico(data);
        }).fail(function() {
            console.error("Error al obtener los datos");
        });
    });

    // Función para mostrar el gráfico utilizando Chart.js
    function mostrarGrafico(datos) {
        console.log("Mostrar gráfico con datos:", datos);
        $("#grafico1").addClass("mostrar");
        var ctx = document.getElementById("miGrafico").getContext("2d");
        var myChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: Object.keys(datos),
                datasets: [
                    {
                        label: "Cantidad de listados por barrio",
                        data: Object.values(datos),
                        backgroundColor: [
                            "rgba(255, 99, 132, 0.2)",
                            "rgba(54, 162, 235, 0.2)",
                            "rgba(255, 206, 86, 0.2)",
                            "rgba(75, 192, 192, 0.2)",
                            "rgba(153, 102, 255, 0.2)",
                        ],
                        borderColor: [
                            "rgba(255, 99, 132, 1)",
                            "rgba(54, 162, 235, 1)",
                            "rgba(255, 206, 86, 1)",
                            "rgba(75, 192, 192, 1)",
                            "rgba(153, 102, 255, 1)",
                        ],
                        borderWidth: 1,
                    },
                ],
            },
        });
    }
});
