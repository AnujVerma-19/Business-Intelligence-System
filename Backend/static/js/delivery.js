document.addEventListener("DOMContentLoaded", function () {

    const canvas = document.getElementById("deliveryStatusChart");

    if (!canvas) {
        return;
    }

    const deliveryData = JSON.parse(
        canvas.dataset.status
    );

    const labels = deliveryData.map(item => item.delivery_status);
    const values = deliveryData.map(item => Number(item.total));

    new Chart(canvas, {
        type: "doughnut",

        data: {
            labels: labels,

            datasets: [{
                label: "Deliveries",
                data: values,
                borderWidth: 1
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

});