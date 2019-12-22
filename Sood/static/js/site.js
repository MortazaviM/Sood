// Total
function IndexFunction(TotalIndexData, HamvaznIndexData, FiftyIndexData, FaraIndexData) {
    var myChart = Highcharts.chart('TotalIndex', {
        chart: {
            type: 'area'
        },
        title: {
            text: 'شاخص کل',
        },
        tooltip: {
            crosshairs: [true, true],
            formatter: function () {
                return this.y;
            }
        },
        xAxis: {
            gridLineWidth: 1
        },
        series: [{
            data: TotalIndexData,
            name: 'شاخص کل',
            color: '#88e',
            fillColor: {
                pattern: {
                    color: '#11d'
                }
            }

        }]
    });



    var myChart = Highcharts.chart('HamvaznIndex', {
        chart: {
            type: 'area'
        },
        title: {
            text: 'شاخص هم وزن',
        },
        tooltip: {
            crosshairs: [true, true],
            formatter: function () {
                return this.y;
            }
        },
        xAxis: {
            gridLineWidth: 1
        },
        series: [{
            data: HamvaznIndexData,
            name: 'شاخص هم وزن',
            color: '#88e',
            fillColor: {
                pattern: {
                    color: '#11d'
                }
            }

        }]
    });


    var myChart = Highcharts.chart('FiftyIndex', {
        chart: {
            type: 'area'
        },
        title: {
            text: 'شاخص 50 شرکت برتر',
        },
        tooltip: {
            crosshairs: [true, true],
            formatter: function () {
                return this.y;
            }
        },
        xAxis: {
            gridLineWidth: 1
        },
        series: [{
            data: FiftyIndexData,
            name: 'شاخص 50 شرکت برتر',
            color: '#88e',
            fillColor: {
                pattern: {
                    color: '#11d'
                }
            }

        }]
    });


    var myChart = Highcharts.chart('FaraIndex', {
        chart: {
            type: 'area'
        },
        title: {
            text: 'شاخص فرابوس',
        },
        tooltip: {
            crosshairs: [true, true],
            formatter: function () {
                return this.y;
            }
        },
        xAxis: {
            gridLineWidth: 1
        },
        series: [{
            data: FaraIndexData,
            name: 'شاخص فرابورس',
            color: '#88e',
            fillColor: {
                pattern: {
                    color: '#11d'
                }
            }

        }]
    });


};
