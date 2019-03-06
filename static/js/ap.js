function ap1(MYCHART, ap) {
	switch (ap) {
		case '14E4E6E173FE':
			var locSeries = [];
			$.ajax({
				type: "get",
				url: "http://localhost:8000/polls/loc/14E4E6E173FE/0",
				async: true,
				success: function(d) {
					$.each(d.data, function(index, item) {
						locSeries.push({"type": "line", "data": item});
					});
					locSeries.push({"type": "line", "markLine": {"data": [{"yAxis": 3000}], "silent": true}})
					var option = {
						title: {
						    text: '按地点聚类效果图1'
						},
						backgroundColor: '#fff',
						tooltip: {},
						// legend: {
						//     data:['销量']
						// },
						xAxis: {
							name: '时间',
			        		data: ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
						},
						yAxis: {
							name: '人次'
						},
						series: locSeries
					};
					MYCHART.setOption(option);
				}
			});
			break;
		case '0857004127E2':
			var locSeries = [];
			$.ajax({
				type: "get",
				url: "http://localhost:8000/polls/loc/0857004127E2/0",
				async: true,
				success: function(d) {
					$.each(d.data, function(index, item) {
						locSeries.push({"type": "line", "data": item});
					});
					// locSeries.push({"type": "line", "markLine": {"data": [{"yAxis": 3000}], "silent": true}})
					var option = {
						title: {
						    text: '按地点聚类效果图1'
						},
						backgroundColor: '#fff',
						tooltip: {},
						// legend: {
						//     data:['销量']
						// },
						xAxis: {
							name: '时间',
			        		data: ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
						},
						yAxis: {
							name: '人次'
						},
						series: locSeries
					};
					MYCHART.setOption(option);
				}
			});
			break;
	}
}

function ap2(MYCHART, ap) {
	switch (ap) {
		case '14E4E6E173FE':
			var locSeries = [];
			$.ajax({
				type: "get",
				url: "http://localhost:8000/polls/loc/14E4E6E173FE/1",
				async: true,
				success: function(d) {
					$.each(d.data, function(index, item) {
						locSeries.push({"type": "line", "data": item});
					});
					locSeries.push({"type": "line", "markLine": {"data": [{"yAxis": 3000}], "silent": true}})
					var option = {
						title: {
						    text: '按地点聚类效果图2'
						},
						backgroundColor: '#fff',
						tooltip: {},
						// legend: {
						//     data:['销量']
						// },
						xAxis: {
							name: '时间',
			        		data: ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
						},
						yAxis: {
							name: '人次'
						},
						series: locSeries
					};
					MYCHART.setOption(option);
				}
			});
			break;
		case '0857004127E2':
			var locSeries = [];
			$.ajax({
				type: "get",
				url: "http://localhost:8000/polls/loc/0857004127E2/1",
				async: true,
				success: function(d) {
					$.each(d.data, function(index, item) {
						locSeries.push({"type": "line", "data": item});
					});
					// locSeries.push({"type": "line", "markLine": {"data": [{"yAxis": 3000}], "silent": true}})
					var option = {
						title: {
						    text: '按地点聚类效果图2'
						},
						backgroundColor: '#fff',
						tooltip: {},
						// legend: {
						//     data:['销量']
						// },
						xAxis: {
							name: '时间',
			        		data: ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
						},
						yAxis: {
							name: '人次'
						},
						series: locSeries
					};
					MYCHART.setOption(option);
				}
			});
			break;
	}
}

function ap5(MYCHART, ap) {
	switch (ap) {
		case '14E4E6E173FE':
			$.ajax({
				type: "get",
				url: "http://localhost:8000/polls/loc/0",
				async: true,
				success: function(d) {
					var option = {
					    title: {
					        text: '占比'
					    },
					    tooltip: {
					    	formatter: '{d}%'
					    },
					    series: [
					    	{
					    		type: 'pie',
					    		data: [
					    			{
					    				value: 6,
					    				name: '非常繁忙'
					    			},
					    			{
					    				value: 7,
					    				name: '有点繁忙'
					    			},
					    			{
					    				value: 8,
					    				name: '一般'
					    			},
					    			{
					    				value: 6,
					    				name: '有点清闲'
					    			},
									{
					    				value: 3,
					    				name: '非常清闲'
					    			}
					    		]
					    	}
					    ]
					};
					MYCHART.setOption(option);
				}
			});
			break;
		case '0857004127E2':
			$.ajax({
				type: "get",
				url: "http://localhost:8000/polls/loc/1",
				async: true,
				success: function(d) {
					var option = {
					    title: {
					        text: '占比'
					    },
						tooltip: {
					    	formatter: '{d}%'
					    },
					    series: [
					    	{
					    		type: 'pie',
					    		data: [
				    			{
				    				value: 6,
				    				name: '非常繁忙'
				    			},
				    			{
				    				value: 7,
				    				name: '有点繁忙'
				    			},
				    			{
				    				value: 8,
				    				name: '一般'
				    			},
				    			{
				    				value: 6,
				    				name: '有点清闲'
				    			},
								{
				    				value: 3,
				    				name: '非常清闲'
				    			}
					    		]
					    	}
					    ]
					};
					MYCHART.setOption(option);
				}
			});
			break;
	}
}

function cc(MYCHART, type) {
	switch (type) {
		case '人多':
			var mock = getVirtulData();
			// console.log(mock);
			var opt = {
				title: {
					text: '人流量分布'
				},
				tooltip: {},
				calendar: {
					range: '2017-10',
					cellSize: [60, 60],
					orient: 'vertical',
					yearLabel: {
						show: false
					},
					monthLabel: {
						show: false
					},
					dayLabel: {
						firstDay: 1,
						nameMap: 'cn'
					}
				},
				visualMap: {
				    type: 'piecewise',
					pieces: [
						{gte: 1, lte: 1, color: '#428bca'},
					],
				    orient: 'vertical',
				    textStyle: {
				        color: '#000'
				    }
				},
				series: [
					{
				        type: 'scatter',
				        coordinateSystem: 'calendar',
				        symbolSize: 1,
				        label: {
				        	show: true,
				        	formatter: function (params) {
				        		// console.log(params);
				        		return echarts.number.parseDate(params.value[0]).getDate();
				        	},
				        	color: '#000'
				        },
				        data: mock
				    }, {
				    	type: 'heatmap',
				    	coordinateSystem: 'calendar',
				    	data: mock
				    }
				]
			};
			MYCHART.setOption(opt);
			break;
		case '一般':
			var mock = getVirtulData();
			var opt = {
				title: {
					text: '类别-日期的分布'
				},
				tooltip: {},
				calendar: {
					range: '2017-10',
					cellSize: [60, 60],
					orient: 'vertical',
					yearLabel: {
						show: false
					},
					monthLabel: {
						show: false
					},
					dayLabel: {
						firstDay: 1,
						nameMap: 'cn'
					}
				},
				visualMap: {
				    type: 'piecewise',
					pieces: [
						{gte: 0, lte: 0, color: '#428bca'},
					],
				    orient: 'vertical',
				    textStyle: {
				        color: '#000'
				    }
				},
				series: [
					{
				        type: 'scatter',
				        coordinateSystem: 'calendar',
				        symbolSize: 1,
				        label: {
				        	show: true,
				        	formatter: function (params) {
				        		return echarts.number.parseDate(params.value[0]).getDate();
				        	},
				        	color: '#000'
				        },
				        data: mock
				    }, {
				    	type: 'heatmap',
				    	coordinateSystem: 'calendar',
				    	data: mock
				    }
				]
			};
			MYCHART.setOption(opt);
			break;
		case '人少':
			var mock = getVirtulData();
			var opt = {
				title: {
					text: '类别-日期的分布'
				},
				tooltip: {},
				calendar: {
					range: '2017-10',
					cellSize: [60, 60],
					orient: 'vertical',
					yearLabel: {
						show: false
					},
					monthLabel: {
						show: false
					},
					dayLabel: {
						firstDay: 1,
						nameMap: 'cn'
					}
				},
				visualMap: {
				    type: 'piecewise',
					pieces: [
						{gte: 2, lte: 2, color: '#428bca'},
					],
				    orient: 'vertical',
				    textStyle: {
				        color: '#000'
				    }
				},
				series: [
					{
				        type: 'scatter',
				        coordinateSystem: 'calendar',
				        symbolSize: 1,
				        label: {
				        	show: true,
				        	formatter: function (params) {
				        		return echarts.number.parseDate(params.value[0]).getDate();
				        	},
				        	color: '#000'
				        },
				        data: mock
				    }, {
				    	type: 'heatmap',
				    	coordinateSystem: 'calendar',
				    	data: mock
				    }
				]
			};
			MYCHART.setOption(opt);
			break;
	}
}

function getVirtulData() {
    var date = +echarts.number.parseDate('2017-10-01');
    var end = +echarts.number.parseDate('2017-11-01');
    var data = [];
    var idx = 0;
    var dayTime = 3600 * 24 * 1000;
    var mock = [2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1];
    // var mock = [6279, 2212, 4753, 2341, 864, 3325, 4904, 2346, 1146, 1972, 629, 4739, 5300, 1943, 657, 1001, 447, 5957, 2413, 3833, 6214, 4295, 4295, 5976, 313, 1353, 1099, 3049, 2809, 2109, 5686];
    for (var time = date; time < end; time += dayTime) {
        data.push([
            echarts.format.formatTime('yyyy-MM-dd', time),
            mock[idx]
        ]);
        idx += 1;
    }
    return data;
}

function box(MYCHART, type) {
	var xAxis = ['0', '1', '2', '3', '4'];
	var yAxis = ['0', '1', '2', '3', '4', '5', '6', '7'];
	// var mock = [[0, 0, 1782], [1, 0, 3810], [2, 0, 2112], [3, 0, 1119], [4, 0, 553], [0, 1, 1847], [1, 1, 5517], [2, 1, 4756], [3, 1, 5702], [4, 1, 3919], [0, 2, 48], [1, 2, 1807], [2, 2, 3283], [3, 2, 1470], [4, 2, 1103], [0, 3, 5284], [1, 3, 5111], [2, 3, 3913], [3, 3, 1206], [4, 3, 4905], [0, 4, 3585], [1, 4, 3345], [2, 4, 6133], [3, 4, 4420], [4, 4, 3163], [0, 5, 1818], [1, 5, 3528], [2, 5, 5255], [3, 5, 5765], [4, 5, 5221], [0, 6, 5209], [1, 6, 1653], [2, 6, 1354], [3, 6, 2723], [4, 6, 3945], [0, 7, 6024], [1, 7, 2846], [2, 7, 3523], [3, 7, 4924], [4, 7, 99]];
	var mock = [[0, 0, 1], [1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 1, 1], [0, 2, 1], [1, 2, 1], [2, 2, 1], [3, 2, 1], [4, 2, 1], [0, 3, 1], [1, 3, 1], [2, 3, 1], [3, 3, 1], [4, 3, 1], [0, 4, 1], [1, 4, 1], [2, 4, 1], [3, 4, 1], [4, 4, 1], [0, 5, 1], [1, 5, 1], [2, 5, 1], [3, 5, 1], [4, 5, 1], [0, 6, 1], [1, 6, 1], [2, 6, 1], [3, 6, 1], [4, 6, 0], [0, 7, 1], [1, 7, 1], [2, 7, 0], [3, 7, 1], [4, 7, 1]];
	var aps = ['0C8268F17F60', '14E4E6E179F2', '0C8268EE38EE', '0C8268C7D504', '0C8268EE3F32', '0C8268C7DD6C', '388345A236BE', '085700411A86', '0C8268F1648E', '0C8268F15C64', '0C8268F93B0A', '0C8268EE3878', '14E4E6E1790A', '14E4E6E16E7A', '0C8268C7E138', '0857004127E2', '0C8268EE7164', '0C8268F933A2', 'EC172FE3B340', '5C63BFD90AE2', '14E4E6E1867A', '0C8268F17FB8', '14E4E6E186A4', '0C8268F15CB2', '14CF924A98F2', '0C8268F9314E', '085700412D4E', '0C8268EE3868', '14E4E6E17A34', '14E6E4E1C510', '0C8268F90E64', '14E4E6E173FE', '14E4E6E17648', '0C8268C804F8', '14E4E6E18658', '14E4E6E172EA', '14E4E6E17908', '14E4E6E17950', '14E4E6E176C8', '0C8268C7D518'];
	switch (type) {
		case '人多':
			var opt = {
				title: {
					text: '类别-AP的分布'
				},
				tooltip: {
					formatter: function(d) {
						var idx = d.value[0] + d.value[1] * 5;
						return aps[idx];
					}
				},
				xAxis: {
					show: false,
					type: 'category',
					data: xAxis,
					min: -1,
					max: 5
				},
				yAxis: {
					show: false,
					type: 'category',
					data: yAxis,
					min: -1,
					max: 8
				},
				visualMap: {
					type: 'piecewise',
					pieces: [
						// {gte: 0, lt: 2000, color: '#0f0'},
						// {gte: 2000, lt: 4000, color: '#ff0'},
						// {gte: 4000, color: '#f00'},
						{gte: 0, lt: 1, color: '#f00'},
						{gte: 1, color: '#0f0'},
					],
					orient: 'vertical',
					textStyle: {
						color: '#000'
					}
				},
				series: [{
					type: 'heatmap',
					data: mock
				}]
			};
			MYCHART.setOption(opt);
			break;
		case '一般':
			var opt = {
				title: {
					text: '类别-AP的分布'
				},
				tooltip: {},
				xAxis: {
					show: false,
					type: 'category',
					data: xAxis,
					min: -1,
					max: 5
				},
				yAxis: {
					show: false,
					type: 'category',
					data: yAxis,
					min: -1,
					max: 8
				},
				visualMap: {
					type: 'piecewise',
					pieces: [
						{gte: 0, lt: 1, color: '#f00'},
						{gte: 1, color: '#0f0'},
					],
					orient: 'vertical',
					textStyle: {
						color: '#000'
					}
				},
				series: [{
					type: 'heatmap',
					data: mock
				}]
			};
			MYCHART.setOption(opt);
			break;
		case '人少':
			var opt = {
				title: {
					text: '类别-AP的分布'
				},
				tooltip: {},
				xAxis: {
					show: false,
					type: 'category',
					data: xAxis,
					min: -1,
					max: 5
				},
				yAxis: {
					show: false,
					type: 'category',
					data: yAxis,
					min: -1,
					max: 8
				},
				visualMap: {
					type: 'piecewise',
					pieces: [
						{gte: 0, lt: 1, color: '#f00'},
						{gte: 1, color: '#0f0'},
					],
					orient: 'vertical',
					textStyle: {
						color: '#000'
					}
				},
				series: [{
					type: 'heatmap',
					data: mock
				}]
			};
			MYCHART.setOption(opt);
			break;
	}
}

$(".one").change(function() {
	var ap = $( ".one option:selected" ).val();

	var dd = document.getElementById('ap1');
	var dd1 = document.getElementById('ap2');
	var dd2 = document.getElementById('ap5');

	dd.removeAttribute("_echarts_instance_");
	dd1.removeAttribute("_echarts_instance_");
	dd2.removeAttribute("_echarts_instance_");

	var echartsAp1 = echarts.init(dd);
	var echartsAp2 = echarts.init(dd1);
	var echartsAp5 = echarts.init(dd2);

	ap1(echartsAp1, ap);
	ap2(echartsAp2, ap);
	ap5(echartsAp5, ap);
}).change();

$(".ss").change(function() {
	var type = $( ".ss option:selected" ).val();

	var dd = document.getElementById('calendar');
	var dd1 = document.getElementById('heatmap');

	dd.removeAttribute("_echarts_instance_");
	dd1.removeAttribute("_echarts_instance_");

	var ec1 = echarts.init(dd);
	var ec2 = echarts.init(dd1);

	cc(ec1, type);
	box(ec2, type);
}).change();