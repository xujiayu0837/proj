var pageNo = 1;
var totalPage = 1;
var limit = 10;
getApList();
$(document).on('click', '.next', function() {
	if (pageNo < totalPage) {
		pageNo += 1;
		getApList();
	}
});
$(document).on('click', '.previous', function() {
	if (pageNo > 1) {
		pageNo -= 1;
		getApList();
	}
});

function getApList() {
	var offset = (pageNo - 1) * limit;
	$.ajax({
		type: "post",
		url: "http://localhost:8000/polls/get-ap-list",
		async: true,
		data: {
			"offset": offset,
			"limit": limit
		},
		dataType: "json",
		success: function(d) {
			var tbody = "";
			var ul = "";
			var data = d.data;
			var totalAp = data.total_num;
			var apList = data.ap_list;
			totalPage = Math.ceil(totalAp / limit);
			for (var i = 0; i < apList.length; i++) {
				tbody = tbody 
				+ "<tr><td>" 
				+ apList[i][0]
				+ "</td><td>"
				+ apList[i][1]
				+ "</td><td>"
				+ apList[i][2]
				+ "</td><td><button type='button' class='btn btn-info'>编辑</button></td><td><button type='button' class='btn btn-danger'>删除</button></td></tr>";
			}
			switch (pageNo) {
				case 1:
					ul = "<li class='previous disabled'><a>&larr; 上一页</a></li><li class='next'><a href='#'>下一页 &rarr;</a></li>";
					break;
				case totalPage:
					ul = "<li class='previous'><a href='#'>&larr; 上一页</a></li><li class='next disabled'><a>下一页 &rarr;</a></li>";
					break;
				default:
					ul = "<li class='previous'><a href='#'>&larr; 上一页</a></li><li class='next'><a href='#'>下一页 &rarr;</a></li>";
			}
			$("#tbody").html(tbody);
			$("#pager").html(ul);
		}
	})
}