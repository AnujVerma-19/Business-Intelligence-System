document.addEventListener("DOMContentLoaded", function () {

    const canvas = document.getElementById("monthlySalesChart");
    const dataElement = document.getElementById("monthlySalesData");

    if (!canvas || !dataElement) {
        return;
    }

    let monthlyData = [];

    try {
        monthlyData = JSON.parse(dataElement.textContent);
    } catch (error) {
        console.error("Unable to read monthly sales data:", error);
        return;
    }

    const months = monthlyData.map(item => item.month);
    const salesValues = monthlyData.map(
        item => Number(item.total_sales || 0)
    );

    new Chart(canvas, {
        type: "line",

        data: {
            labels: months,

            datasets: [{
                label: "Monthly Sales",
                data: salesValues,

                borderWidth: 3,
                tension: 0.35,
                fill: true,

                pointRadius: 4,
                pointHoverRadius: 6
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            interaction: {
                intersect: false,
                mode: "index"
            },

            plugins: {
                legend: {
                    display: true,
                    position: "top"
                },

                tooltip: {
                    callbacks: {
                        label: function (context) {
                            return "Sales: ₹" +
                                Number(context.raw).toLocaleString("en-IN");
                        }
                    }
                }
            },

            scales: {
                x: {
                    grid: {
                        display: false
                    }
                },

                y: {
                    beginAtZero: true,

                    ticks: {
                        callback: function (value) {
                            return "₹" +
                                Number(value).toLocaleString("en-IN");
                        }
                    }
                }
            }
        }
    });

});