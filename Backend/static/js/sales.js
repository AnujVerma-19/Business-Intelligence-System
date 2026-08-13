document.addEventListener("DOMContentLoaded", function () {

    const canvas = document.getElementById("monthlySalesChart");
    const dataElement = document.getElementById("monthlySalesData");

    if (!canvas || !dataElement) {
        return;
    }

    const monthlyData = JSON.parse(dataElement.textContent);

    const months = monthlyData.map(item => item.month);
    const salesValues = monthlyData.map(item => Number(item.total_sales));

    new Chart(canvas, {
        type: "line",

        data: {
            labels: months,

            datasets: [{
                label: "Monthly Sales",
                data: salesValues,
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