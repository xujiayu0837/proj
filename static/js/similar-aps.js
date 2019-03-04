function ap11(MYCHART, ap) {
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
					var option = {
						backgroundColor: '#fff',
						tooltip: {},
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

function ap12(MYCHART, ap) {
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
					var option = {
						backgroundColor: '#fff',
						tooltip: {},
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

function ap21(MYCHART, ap) {
	switch (ap) {
		case '14E4E6E1790A':
			var locSeries = [];
			$.ajax({
				type: "get",
				url: "http://localhost:8000/polls/loc/14E4E6E1790A/0",
				async: true,
				success: function(d) {
					$.each(d.data, function(index, item) {
						locSeries.push({"type": "line", "data": item});
					});
					var option = {
						backgroundColor: '#fff',
						tooltip: {},
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

function ap22(MYCHART, ap) {
	switch (ap) {
		case '14E4E6E1790A':
			var locSeries = [];
			$.ajax({
				type: "get",
				url: "http://localhost:8000/polls/loc/14E4E6E1790A/1",
				async: true,
				success: function(d) {
					$.each(d.data, function(index, item) {
						locSeries.push({"type": "line", "data": item});
					});
					var option = {
						backgroundColor: '#fff',
						tooltip: {},
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

var doc11 = document.getElementById('ap11');
var doc12 = document.getElementById('ap12');
var doc21 = document.getElementById('ap21');
var doc22 = document.getElementById('ap22');

var echartsAp11 = echarts.init(doc11);
var echartsAp12 = echarts.init(doc12);
var echartsAp21 = echarts.init(doc21);
var echartsAp22 = echarts.init(doc22);

ap = '14E4E6E173FE'
ap11(echartsAp11, ap);
ap12(echartsAp12, ap);
ap = '14E4E6E1790A'
ap21(echartsAp21, ap);
ap22(echartsAp22, ap);