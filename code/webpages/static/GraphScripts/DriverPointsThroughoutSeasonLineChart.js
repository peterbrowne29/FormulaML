            const xlabels = [];
            const points_data = [];
            makeChart();
            async function makeChart(){
                await getStanding();
                const ctx = document.getElementById('driver_stats').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: xlabels,
                        datasets: [{
                        label: 'Points Earned',
                    data: points_data,
                    fill: false,
                    backgroundColor: [
                        'white',
                    ],
                    borderColor: [
                        'black',
                    ],
                    borderWidth: 1
                                    }]
                            },
                    options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                            }
                            }
                    });
                }
        async function getStanding(){
        const standings = await fetch('data/DriverStandings.csv');
        const data = await standings.text();
        const d_standings = data.split('\n');
        const year_list = [];
        const point_list = [];
        for (var i = 0; i < d_standings.length; i++){
            const row = d_standings[i].split(',');
            const year = row[0]; 
            const round = row[1];
            const driver = row[2];
            const points = row[3];
            if (driver == "max_verstappen" && year == "2020"){
                year_list.push(year);
                point_list.push(points);
                xlabels.push(year);
                points_data.push(point_list[point_list.length -1]);
            }      
        };
        console.log(point_list);
        }