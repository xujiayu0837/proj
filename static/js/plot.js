var userSeries = [];
function user() {
	$.ajax({
		type: "get",
		url: "http://localhost:8000/polls/user/0",
		async: true,
		success: function(d) {
			$.each(d.data, function(index, item) {
				userSeries.push({"type": "line", "data": item});
			});
			// 基于准备好的dom，初始化echarts实例
			var myChart = echarts.init(document.getElementById('user'));

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
			    	name: 'AP',
			    	data: ['R_1','R_1','R_10','R_10','R_3','R_4','R_3','R_5','R_8','R_5','R_29','R_2','R_2','R_10','R_29','R_4','T_1','S_2','T_4','T_4','S_2','S_1','T_6','S_1','T_1','T_3','T_3','R_8']
			    },
			  //   xAxis: {
					// data: ['mac_1', 'mac_2', 'mac_3', 'mac_4', 'mac_5', 'mac_6', 'mac_7', 'mac_8', 'mac_9', 'mac_10', 'mac_11', 'mac_12', 'mac_13', 'mac_14', 'mac_15', 'mac_16', 'mac_17', 'mac_18', 'mac_19', 'mac_20', 'mac_21', 'mac_22', 'mac_23', 'mac_24', 'mac_25', 'mac_26', 'mac_27', 'mac_28', 'mac_29', 'mac_30', 'mac_31', 'mac_32', 'mac_33', 'mac_34', 'mac_35', 'mac_36', 'mac_37', 'mac_38', 'mac_39', 'mac_40']
			  //   },
			    yAxis: {
			    	name: 'rss'
			    },
			    series: userSeries
			    // series: [
			    // 	{
			    // 		type: 'line',
			    // 		data: [-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-46.666666666666664,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-65.0]
			    // 	},
			    // 	{
			    // 		type: 'line',
			    // 		data: [-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-73.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-60.0]
			    // 	},
			    // 	{
			    // 		type: 'line',
			    // 		data: [-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-55.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0]
			    // 	},
			    // 	{
			    // 		type: 'line',
			    // 		data: [-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-65.6875,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-87.1875]
			    // 	},
			    // 	{
			    // 		type: 'line',
			    // 		data: [-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-80.5,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-51.5]
			    // 	},
			    // 	{
			    // 		type: 'line',
			    // 		data: [-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-89.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-90.0,-60.916666666666664]
			    // 	}
			    // ]
			};

			// 使用刚指定的配置项和数据显示图表。
			myChart.setOption(option);
		}
	});
}
user()

var periodSeries = [];
function period() {
	$.ajax({
		type: "get",
		url: "http://localhost:8000/polls/period/am/0",
		async: true,
		success: function(d) {
			$.each(d.data, function(index, item) {
				periodSeries.push({"type": "line", "data": item});
			});
			var myChart = echarts.init(document.getElementById('period1'));
			var option = {
			    title: {
			        text: '按时间聚类效果图（7:00-9:00）'
			    },
			    backgroundColor: '#fff',
			    tooltip: {},
			    // legend: {
			    //     data:['销量']
			    // },
			    xAxis: {
			    	name: 'AP',
			        data: ['R_10','R_10','R_2','S_2','S_2']
			    },
			    yAxis: {
			    	name: '次数'
			    },
			    series: periodSeries
			};
			myChart.setOption(option);
		}
	});
}
period()

var periodSeries2 = [];
function period2() {
	$.ajax({
		type: "get",
		url: "http://localhost:8000/polls/period/noon/1",
		async: true,
		success: function(d) {
			$.each(d.data, function(index, item) {
				periodSeries2.push({"type": "line", "data": item});
			});
			var myChart = echarts.init(document.getElementById('period2'));
			var option = {
			    title: {
			        text: '按时间聚类效果图（11:00-13:00）'
			    },
			    backgroundColor: '#fff',
			    tooltip: {},
			    // legend: {
			    //     data:['销量']
			    // },
			    xAxis: {
			    	name: 'AP',
			        data: ['R_10','R_29','R_2','R_2','R_29','T_1','S_2','S_2','S_1','T_6','T_3']
			    },
			    yAxis: {
			    	name: '次数'
			    },
			    series: periodSeries2
			};
			myChart.setOption(option);
		}
	});
}
period2()

var periodSeries3 = [];
function period3() {
	$.ajax({
		type: "get",
		url: "http://localhost:8000/polls/period/pm/0",
		async: true,
		success: function(d) {
			$.each(d.data, function(index, item) {
				periodSeries3.push({"type": "line", "data": item});
			});
			var myChart = echarts.init(document.getElementById('period3'));
			var option = {
			    title: {
			        text: '按时间聚类效果图（17:00-19:00）'
			    },
			    backgroundColor: '#fff',
			    tooltip: {},
			    // legend: {
			    //     data:['销量']
			    // },
			    xAxis: {
			    	name: 'AP',
			        data: ['R_10','R_3','R_4','R_3','R_5','R_8','R_5','R_2','R_2','R_10','R_4','T_1','S_2','S_1','S_1']
			    },
			    yAxis: {
			    	name: '次数'
			    },
			    series: periodSeries3
			};
			myChart.setOption(option);
		}
	});
}
period3()

var locSeries = [];
function loc() {
	$.ajax({
		type: "get",
		url: "http://localhost:8000/polls/loc/0",
		async: true,
		success: function(d) {
			$.each(d.data, function(index, item) {
				locSeries.push({"type": "line", "data": item});
			});
			var myChart = echarts.init(document.getElementById('loc1'));
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
			        data: ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
			    },
			    yAxis: {
			    	name: '人次'
			    },
			    series: locSeries
			  //   series: [
			  //       {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [32,12,9,0,3,16,46,234,382,461,554,1095,1691,814,554,703,758,1459,1643,1003,492,376,125,51]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [17,6,10,2,4,12,82,186,551,289,339,1134,1415,556,237,319,417,1233,1078,571,257,257,144,65]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [18,7,8,4,21,18,56,260,400,389,545,1168,1266,648,384,608,1034,1723,1200,579,605,398,152,67]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [35,4,3,3,5,16,66,396,470,324,378,846,1508,650,613,853,867,1286,1847,1038,550,404,155,79]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [20,5,4,4,9,21,42,346,476,676,803,937,1208,825,891,1219,1270,1788,1255,580,416,356,131,74]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [10,5,6,7,7,16,50,359,800,516,546,1429,1953,1013,693,585,999,1421,1280,824,517,264,209,39]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [26,12,4,5,5,15,61,262,684,623,655,1515,1914,732,483,369,632,2026,1350,850,594,346,229,103]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [23,4,8,7,11,10,39,299,703,636,536,2204,2771,986,291,173,361,1877,1409,612,291,283,257,73]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [25,6,8,14,6,18,87,302,828,1131,1277,2529,2946,1096,534,809,618,2045,1460,762,575,433,279,120]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [25,7,7,3,9,10,204,558,1007,1169,1101,1972,2614,1296,1001,763,1365,2313,1812,1385,970,595,268,182]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [52,13,5,9,12,19,241,657,723,852,765,2301,2272,1052,838,886,1249,2055,1673,1069,650,629,373,172]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [62,14,7,4,7,23,84,516,979,1056,1233,1791,2467,1319,948,680,878,1444,1408,983,648,332,206,186]
			  //       },
					// {
			  //           // name: '销量',
			  //           type: 'line',
			  //           data: [91,11,2,2,5,20,108,565,896,940,924,1960,2650,1229,998,1262,1076,1827,1605,1167,38,0,0,0]
			  //       }
			  //   ]
			};
			myChart.setOption(option);
		}
	});
}
loc()

var locSeries2 = [];
function loc2() {
	$.ajax({
		type: "get",
		url: "http://localhost:8000/polls/loc/1",
		async: true,
		success: function(d) {
			$.each(d.data, function(index, item) {
				locSeries2.push({"type": "line", "data": item});
			});
			var myChart = echarts.init(document.getElementById('loc2'));
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
			        data: ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
			    },
			    yAxis: {
			    	name: '人次'
			    },
			    series: locSeries2
			};
			myChart.setOption(option);
		}
	});
}
loc2()