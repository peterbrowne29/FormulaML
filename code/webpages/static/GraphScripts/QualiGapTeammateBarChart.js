            const chartOptions = {
            scales: {
                    yAxes: [{barPercentage: 0.5}]
                    },
                    elements: {
                    rectangle: {
                    borderSkipped: 'left',}}};
            const colours = [];
            const xlabels = [];
            const points_data = [];

            makeChart();
            async function makeChart(){
                await getStanding();
                const ctx = document.getElementById('TeamPoints_stats').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: xlabels,
                        datasets: [{
                        label: 'Qualifying Gap to Teammate 2020 (Lower is better)',
                        data: points_data,
                        backgroundColor: colours,
                        fill: false,
                        borderWidth: 1
                                        }]
                            },
                    options: { chartOptions,
                        scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                suggestedMin: -1,
                                suggestedMax: 1
                                
                            }
                        }]
                            }
                            }
                    });
                }

        var dynamicColors = function() {
        var r = 6
        var g = 0
        var b = 239
            return "rgb(" + r + "," + g + "," + b + ")";
        };

        async function getStanding(){
        const standings = await fetch('../../Data/QualiComparison/HAM.csv');
        const data = await standings.text();
        const d_standings = data.split('\n');
        const rounds = [];
        const times = [];
        for (var i = 0; i < d_standings.length; i++){
            const row = d_standings[i].split(',');
            const round = row[0];
            const time = row[1];
                points_data.push(time);
                console.log(time);
                xlabels.push(round);
                colours.push(dynamicColors());
            }    
        };