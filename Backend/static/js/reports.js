ddocument.addEventListener("DOMContentLoaded", function () {

    const canvas = document.getElementById("reportMonthlySalesChart");

    if (!canvas) {
        console.log("Monthly Sales canvas not found");
        return;
    }

    const salesData = JSON.parse(canvas.dataset.sales);

    console.log("Monthly Sales Data:", salesData);

    const labels = salesData.map(item => item.month);

    const values = salesData.map(item => Number(item.total_sales));

    new Chart(canvas, {

        type: "line",

        data: {

            labels: labels,

            datasets: [{
                label: "Monthly Sales",
                data: values,
                borderWidth: 2,
                tension: 0.3,
                fill: false
            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            scales: {

                y: {
                    beginAtZero: true
                }

            }

        }

    });

});