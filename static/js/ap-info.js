function getApList() {
	$.ajax({
		type: "get",
		url: "http://localhost:8000/polls/get-ap-list",
		async: true,
		success: function(d) {
			var tbody = "";
			var data = d.data;
			for (var i = 0; i < data.length; i++) {
				tbody = tbody 
				+ "<tr><td>" 
				+ data[i][0]
				+ "</td><td>"
				+ data[i][1]
				+ "</td><td>"
				+ data[i][2]
				+ "</td><td>操作</td><td>操作</td></tr>";
			}
			$("#tbody").html(tbody);
		}
	})
}

getApList()