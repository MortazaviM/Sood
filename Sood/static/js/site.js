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



function StockFunction(myData, ma5, ma10, ma20, ma50,myDate) {
    var myChart = Highcharts.chart('StockChart', {
        chart: {
            type: 'line',
            zoomType: 'xy',
        },
        plotOptions: {
            series: {
                marker: {
                    enabled: false
                }
            }
        },
        title: {
            text: "نمودار سهم بر مبنای قیمت پایانی",
        },
        tooltip: {
            crosshairs: [true, true],
            formatter: function () {
                return "قیمت: " + this.y + " در تاریخ: " + this.x;
            }
        },
        xAxis: {

            categories:myDate,
            crosshair: true,
        },
        series: [            
            {
            type: 'line',
            data: myData,
            name: 'قیمت پایانی سهم',
            color: '#008421',
            fillColor: {
                pattern: {
                    color: '#11d'
                }
            },
            marker: {
                enabled: true
            }

        }, {
            data: ma5,
            name: 'میانگین متحرک 5 روزه',
        }, {
            data: ma10,
            name: 'میانگین متحرک 10 روزه',
        }, {
            data: ma20,
            name: 'میانگین متحرک 20 روزه',
        }, {
            data: ma50,
            name: 'میانگین متحرک 50 روزه',
        }]
    });
};