function user1(MYCHART, user) {
	if (user == '000000000000') {
		var userSeries = [];
		$.ajax({
			type: "get",
			url: "http://localhost:8000/polls/user/0",
			async: true,
			success: function(d) {
				$.each(d.data, function(index, item) {
					userSeries.push({"type": "line", "data": item});
				});
				// 指定图表的配置项和数据
				var option = {
				    title: {
				        text: '按用户聚类效果图'
				    },
				    backgroundColor: '#fff',
				    tooltip: {},
				    // legend: {
				    //     data:['销量']
				    // },
				    xAxis: {
				    	axisLine: {
				    		onZero: false
				    	},
				    	name: 'AP',
				    	data: ['R_1','R_1','R_10','R_10','R_3','R_4','R_3','R_5','R_8','R_5','R_29','R_2','R_2','R_10','R_29','R_4','T_1','S_2','T_4','T_4','S_2','S_1','T_6','S_1','T_1','T_3','T_3','R_8']
				    },
				    yAxis: {
				    	name: 'rss',
				    	scale: true
				    },
				    series: userSeries
				};
				MYCHART.setOption(option);
			}
		});
	} else if (user == '123456') {
		var userSeries = [];
		$.ajax({
			type: "get",
			url: "http://localhost:8000/polls/user/2",
			async: true,
			success: function(d) {
				$.each(d.data, function(index, item) {
					userSeries.push({"type": "line", "data": item});
				});
				// 指定图表的配置项和数据
				var option = {
				    title: {
				        text: '按用户聚类效果图'
				    },
				    backgroundColor: '#fff',
				    tooltip: {},
				    // legend: {
				    //     data:['销量']
				    // },
				    xAxis: {
				    	axisLine: {
				    		onZero: false
				    	},
				    	name: 'AP',
				    	data: ['R_1','R_1','R_10','R_10','R_3','R_4','R_3','R_5','R_8','R_5','R_29','R_2','R_2','R_10','R_29','R_4','T_1','S_2','T_4','T_4','S_2','S_1','T_6','S_1','T_1','T_3','T_3','R_8']
				    },
				    yAxis: {
				    	name: 'rss',
				    	scale: true
				    },
				    series: userSeries
				};
				MYCHART.setOption(option);
			}
		});
	}
}

function user2(MYCHART, user) {
	if (user == '000000000000') {
		var userSeries = [];
		$.ajax({
			type: "get",
			url: "http://localhost:8000/polls/user/1",
			async: true,
			success: function(d) {
				$.each(d.data, function(index, item) {
					userSeries.push({"type": "line", "data": item});
				});
				// 指定图表的配置项和数据
				var option = {
				    title: {
				        text: '按用户聚类效果图'
				    },
				    backgroundColor: '#fff',
				    tooltip: {},
				    // legend: {
				    //     data:['销量']
				    // },
				    xAxis: {
				    	axisLine: {
				    		onZero: false
				    	},
				    	name: 'AP',
				    	data: ['R_1','R_1','R_10','R_10','R_3','R_4','R_3','R_5','R_8','R_5','R_29','R_2','R_2','R_10','R_29','R_4','T_1','S_2','T_4','T_4','S_2','S_1','T_6','S_1','T_1','T_3','T_3','R_8']
				    },
				    yAxis: {
				    	name: 'rss',
				    	scale: true
				    },
				    series: userSeries
				};
				MYCHART.setOption(option);
			}
		});
	} else if (user == '123456') {
		var userSeries = [];
		$.ajax({
			type: "get",
			url: "http://localhost:8000/polls/user/3",
			async: true,
			success: function(d) {
				$.each(d.data, function(index, item) {
					userSeries.push({"type": "line", "data": item});
				});
				// 指定图表的配置项和数据
				var option = {
				    title: {
				        text: '按用户聚类效果图'
				    },
				    backgroundColor: '#fff',
				    tooltip: {},
				    // legend: {
				    //     data:['销量']
				    // },
				    xAxis: {
				    	axisLine: {
				    		onZero: false
				    	},
				    	name: 'AP',
				    	data: ['R_1','R_1','R_10','R_10','R_3','R_4','R_3','R_5','R_8','R_5','R_29','R_2','R_2','R_10','R_29','R_4','T_1','S_2','T_4','T_4','S_2','S_1','T_6','S_1','T_1','T_3','T_3','R_8']
				    },
				    yAxis: {
				    	name: 'rss',
				    	scale: true
				    },
				    series: userSeries
				};
				MYCHART.setOption(option);
			}
		});
	}
}

function user5(MYCHART, user) {
	if (user == '000000000000') {
		$.ajax({
			type: "get",
			url: "http://localhost:8000/polls/user/0",
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
				    				value: 21,
				    				name: '人多'
				    			},
								{
				    				value: 9,
				    				name: '人少'
				    			}
				    		]
				    	}
				    ]
				};
				MYCHART.setOption(option);
			}
		});
	} else if (user == '123456') {
		$.ajax({
			type: "get",
			url: "http://localhost:8000/polls/user/1",
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
				    				value: 21,
				    				name: '人多'
				    			},
								{
				    				value: 9,
				    				name: '人少'
				    			}
				    		]
				    	}
				    ]
				};
				MYCHART.setOption(option);
			}
		});
	}
}

$(".one").change(function() {
	var user = $( ".one option:selected" ).val();

	var dd = document.getElementById('user1');
	var dd1 = document.getElementById('user2');
	var dd2 = document.getElementById('user5');

	dd.removeAttribute("_echarts_instance_");
	dd1.removeAttribute("_echarts_instance_");
	dd2.removeAttribute("_echarts_instance_");

	var echartsAp1 = echarts.init(dd);
	var echartsAp2 = echarts.init(dd1);
	var echartsAp5 = echarts.init(dd2);

	user1(echartsAp1, user);
	user2(echartsAp2, user);
	user5(echartsAp5, user);
}).change();
