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
                        label: 'Points Earned',
                        data: points_data,
                        backgroundColor: colours,
                        fill: false,
                        borderWidth: 1
                                        }]
                            },
                    options: { chartOptions,
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
        const standings = await fetch('data/ConstructorStandings.csv');
        const data = await standings.text();
        const d_standings = data.split('\n');
        const point_list = [];
        const year_list = [];
        const round_list = [];
        for (var i = 0; i < d_standings.length; i++){
            const row = d_standings[i].split(',');
            const year = row[0]; 
            const round = row[1];
            const team = row[2];
            const points = row[3];
            if (team == "red_bull"){
                year_list.push(year);
                point_list.push(points);
                round_list.push(round);
                colours.push(dynamicColors());
            }    
        };
        round_list.push("1");
        for (var i = 1; i < year_list.length && point_list.length; i++){
                if(!xlabels.includes(year_list[i])){
                    xlabels.push(year_list[i]);
                }
                console.log(round_list);
                console.log(point_list);
                if(parseFloat(round_list[i]) > parseFloat(round_list[i + 1])){
                    points_data.push(point_list[i]);
                }
            }
        }
