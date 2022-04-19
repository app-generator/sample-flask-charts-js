const headers = {
                    headers: {'Content-Type': 'application/json'}
                }
fetch("/api/MonthlyCustomers", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['month_name']})
                                        const y = data['data'].map(function(d){ return d['customer_count']})
                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'Monthly Customers',
                                            backgroundColor: 'rgb(255, 99, 132)',
                                            borderColor: 'rgb(255, 99, 132)',
                                            data: y,
                                            }]
                                        };
                                        const config = {
                                            type: 'line',
                                            data: chart_data,
                                            options: {}
                                        };
                                        const linechart = new Chart(
                                            document.getElementById('linechart'),
                                            config
                                        );
                                        console.log(config)
                                    });

fetch("/api/MonthlySales", {
                        method: "GET",
                        headers: headers
                        }).then(response => response.json())
                        .then(data => {
                                        const x = data['data'].map(function(d){ return d['month_name']});
                                        const y = data['data'].map(function(d){ return d['sale']});

                                        const chart_data = {
                                            labels: x,
                                            datasets: [{
                                            label: 'Monthly Sales',
                                            backgroundColor: 'rgb(255, 99, 132)',
                                            borderColor: 'rgb(255, 99, 132)',
                                            data: y,
                                            }]
                                        };
                                        const config = {
                                            type: 'bar',
                                            data: chart_data,
                                            options: {}
                                        };
                                        const monthlySales = new Chart(
                                            document.getElementById('barchart'),
                                            config
                                        );
                                        console.log(config)
                                    });


fetch("/api/ProductSales", {
                            method: "GET",
                            headers: headers
                            }).then(response => response.json())
                            .then(data => {
                                            const x = data['data'].map(function(d){ return d['product']})
                                            const y = data['data'].map(function(d){ return d['sale']})
                                            
                                            const chart_data = {
                                                labels: x,
                                                datasets: [{
                                                label: 'Sale',
                                                backgroundColor: [
                                                    'rgb(255, 99, 132)',
                                                    'rgb(54, 162, 235)',
                                                    'rgb(255, 205, 86)',
                                                    'rgb(150, 205, 86)',
                                                    'rgb(210, 70, 110)',
                                                    'rgb(54, 162, 200)',
                                                    'rgb(220, 150, 86)',
                                                    'rgb(150, 205, 86)',
                                                    
                                                  ],
                                                data: y,
                                                }]
                                            };
                                            const config = {
                                                type: 'pie',
                                                data: chart_data,
                                                options: {}
                                            };
                                            const monthlySales = new Chart(
                                                document.getElementById('piechart'),
                                                config
                                            );
                                            console.log(config)
                                        });                                   