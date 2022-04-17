
const headers = {
                    headers: {'Content-Type': 'application/json'}
                }
fetch("/api/DailySales", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const labels = data['labels'];
                                        const monthly_sales = data['data'];
                                        const chart_data = {
                                            labels: labels,
                                            datasets: [{
                                            label: 'Sale',
                                            backgroundColor: 'rgb(255, 99, 132)',
                                            borderColor: 'rgb(255, 99, 132)',
                                            data: monthly_sales,
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {}
                                        };
                                        const monthlySales = new Chart(
                                            document.getElementById('dailysales'),
                                            config
                                        );
                                        console.log(config)
                                    });

fetch("/api/MonthlySales", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const labels = data['labels'];
                                        const monthly_sales = data['data'];
                                        const chart_data = {
                                            labels: labels,
                                            datasets: [{
                                            label: 'Sale',
                                            backgroundColor: 'rgb(255, 99, 132)',
                                            borderColor: 'rgb(255, 99, 132)',
                                            data: monthly_sales,
                                            }]
                                        };
                                        const config = {
                                            type: 'bar',
                                            data: chart_data,
                                            options: {}
                                        };
                                        const monthlySales = new Chart(
                                            document.getElementById('monthlysales'),
                                            config
                                        );
                                        console.log(config)
                                    });


fetch("/api/SalesByCategory", {
                            method: "GET",
                            headers: headers
                            }).then(response => response.json())
                            .then(data => {
                                            const labels = data['labels'];
                                            const monthly_sales = data['data'];
                                            const chart_data = {
                                                labels: labels,
                                                datasets: [{
                                                label: 'Sale',
                                                backgroundColor: [
                                                    'rgb(255, 99, 132)',
                                                    'rgb(54, 162, 235)',
                                                    'rgb(255, 205, 86)',
                                                    'rgb(150, 205, 86)'
                                                  ],
                                                data: monthly_sales,
                                                }]
                                            };
                                            const config = {
                                                type: 'pie',
                                                data: chart_data,
                                                options: {}
                                            };
                                            const monthlySales = new Chart(
                                                document.getElementById('sales_by_category'),
                                                config
                                            );
                                            console.log(config)
                                        });                                   