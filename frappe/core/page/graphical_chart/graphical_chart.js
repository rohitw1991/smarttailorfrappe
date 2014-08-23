

// frappe.require("/core/page/graphical_chart/api.js");

frappe.pages['graphical-chart'].onload = function(wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Chart'
		// single_column: true
	});

// $(wrapper).find(".layout-main").html("<div class='user-settings'  id ='sp_tab'  style='min-height: 200px;'></div>");
$('<div id="head" style="height:20px; width:800px;" ><b>Sales Details</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));
$("<table class='table table-bordered' style='height:150px; width:800px;'>\
	<tr width='100%'>\
	<td width='50%'><div class='user-settings' style='min-height: 150px;' id ='pie_tab' ></div>\
	</td><td width='50%'><div class='user-settings' style='min-height: 150px;' id ='column_tab' ></div></td>\
	</tr>\
	</table>").appendTo($(wrapper).find(".layout-main-section"));

//for heading
$('<div id="head" style="height:20px; width:800px;" ><b>Revenue Details</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));

//for filters
$('<div id="main" style="height:50px; width:800px;" >\
	<table class="table" style="height:5px; width:800px;" >\
	<tr width="100%"><td width="25%" style="min-height:20px;"><div id ="ctab" text-align="left" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab1" text-align="left" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab2" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab3" style="min-height: 10px;" ></div></td>\
	</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));

//for chart
$("<table class='table table-bordered' style='height:150px; width:800px;'>\
	<tr width='100%'><td width='50%'>\
	<div class='user-settings'  id ='pie_tab2'  style='min-height: 150px;'></div></td>\
	<td width='50%'><div class='user-settings'  id ='column_tab2'  style='min-height: 150px;'></div></td>\
	</tr>\
	</table>").appendTo($(wrapper).find('.layout-main-section'));

//for heading
$('<div id="head" style="height:20px; width:800px;" ><b>Prospects Details</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));
//for filter
$('<div id="main" style="height:50px; width:800px;" >\
	<table class="table" style="height:5px; width:800px;" >\
	<tr width="100%"><td width="25%" style="min-height:20px;"><div id ="ctab22" text-align="left" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab122" text-align="left" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab222" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab322" style="min-height: 10px;" ></div></td>\
	</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));
//for chart
$("<table class='table table-bordered' style='height:150px; width:800px;'>\
	<tr width='100%'><td width='50%'>\
	<div class='user-settings'  id ='pie_tab3'  style='min-height: 150px;'></div></td>\
	<td width='50%'><div class='user-settings'  id ='column_tab3'  style='min-height:150px;'></div></td>\
	</tr>\
	</table>").appendTo($(wrapper).find('.layout-main-section'));
//for heading
$('<div id="head" style="height:20px; width:800px;" ><b>Subscrption Renewal Details</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));
//for forth filter
$('<div id="main" style="height:50px; width:800px;" >\
	<table class="table" style="height:5px; width:800px;" >\
	<tr width="100%"><td width="25%" style="min-height:20px;"><div id ="ctab44" text-align="left" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab144" text-align="left" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab244" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab344" style="min-height: 10px;" ></div></td>\
	</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));


//for chart
$("<table class='table table-bordered' style='height:150px; width:800px;'>\
	<tr width='100%'><td width='50%'>\
	<div class='user-settings'  id ='pie_tab4' style='min-height: 150px;'></div></td>\
	<td width='50%'><div class='user-settings'  id ='column_tab4'  style='min-height: 150px;'></div></td>\
	</tr>\
	</table>").appendTo($(wrapper).find('.layout-main-section'));


//for heading
$('<div id="head" style="height:20px; width:800px;" ><b>New Sales Details</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));

//for fifth filters
$('<div id="main" style="height:50px; width:800px;" >\
	<table class="table" style="height:5px; width:800px;" >\
	<tr width="100%"><td width="25%" style="min-height:20px;"><div id ="ctab55" text-align="left" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab155" text-align="left" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab255" style="min-height: 10px;" ></div></td>\
	<td width="25%"><div id ="ctab355" style="min-height: 10px;" ></div></td>\
	</tr></table></div>').appendTo($(wrapper).find('.layout-main-section'));


//for fifth chart
$("<table class='table table-bordered' style='height:40px; width:800px;'>\
	<tr width='100%'><td width='50%'>\
	<div class='user-settings'  id ='pie_tab5' style='min-height: 180px;'></div></td>\
	<td width='50%'><div class='user-settings'  id ='column_tab5'  style='min-height: 200px;'></div></td>\
	</tr>\
	</table>").appendTo($(wrapper).find('.layout-main-section'));
//for side section
$("<div id='side'></div>").appendTo($(wrapper).find('.layout-side-section'));

wrapper.this = new frappe.Chart(wrapper);	
}

frappe.Chart = Class.extend({
	init: function(wrapper) {
		this.wrapper = wrapper;
		this.body = $(this.wrapper).find(".user-settings");
		this.make_link();
		this.make_menu();
		this.make_menu2();
		this.make_menu4();
		this.make_menu5();
		this.make_pie_chart()
		this.make_column_chart()
		this.make_pie_chart2()
		this.make_column_chart2()
		this.make_pie_chart3()
		this.make_column_chart3()
		this.make_pie_chart4()
		this.make_column_chart4()
		this.make_pie_chart5()
		this.make_column_chart5()
		this.show_active_users()
	
		// $(this.wrapper).find('.layout-main-section').css({"height": "100px"});
		// $(this.wrapper).find('.layout-main').css("width","700px");
		// $("<html><head>Hi</head></html>").appendTo($(wrapper).find('.layout-side-section'));

		},
	make_pie_chart:function(from_date,to_date){
		console.log("in the fun");
		frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(r.message);
			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		   	 for(var x in r.message.sales_order_total){
  				mydata.push(r.message.sales_order_total[x]);
               }
               // console.log(mydata)
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Sales Activities'
		    };
		    var chart = new google.visualization.PieChart(document.getElementById('pie_tab'));
		    chart.draw(data, options);
		  }
		  	}
	    });
		},

	make_column_chart:function(from_date,to_date){
		    frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));
			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		  	 // console.log(r.message.sales_order_total[0]);
		  	 for(var x in r.message.sales_order_total){
  				mydata.push(r.message.sales_order_total[x]);
               }
               // console.log(mydata)
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Sales Activities'
		    };
		    var chart = new google.visualization.ColumnChart(document.getElementById("column_tab"));
		    chart.draw(data, options);
		    }
		    }
	    });
	},
		make_pie_chart3:function(from_date,to_date){
		console.log("in the fun");
		frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));
			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		   	 for(var x in r.message.sales_order_total){
  				mydata.push(r.message.sales_order_total[x]);
               }
               // console.log(mydata)
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Sales Activities'
		    };
		    var chart = new google.visualization.PieChart(document.getElementById('pie_tab3'));
		    chart.draw(data, options);
		  }
		  	}
	    });
		},

	make_column_chart3:function(from_date,to_date){
		    frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));
			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		  	 // console.log(r.message.sales_order_total[0]);
		  	 for(var x in r.message.sales_order_total){
  				mydata.push(r.message.sales_order_total[x]);
               }
               // console.log(mydata)
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Sales Activities'
		    };
		    var chart = new google.visualization.ColumnChart(document.getElementById("column_tab3"));
		    chart.draw(data, options);
		    }
		    }
	    });
	},
	make_pie_chart4:function(from_date,to_date){
		console.log("in the fun");
		frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));
			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		   	 for(var x in r.message.sales_order_total){
  				mydata.push(r.message.sales_order_total[x]);
               }
               // console.log(mydata)
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Sales Activities'
		    };
		    var chart = new google.visualization.PieChart(document.getElementById('pie_tab4'));
		    chart.draw(data, options);
		  }
		  	}
	    });
		},

	make_column_chart4:function(from_date,to_date){
		    frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));
			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		  	 // console.log(r.message.sales_order_total[0]);
		  	 for(var x in r.message.sales_order_total){
  				mydata.push(r.message.sales_order_total[x]);
               }
               // console.log(mydata)
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Sales Activities'
		    };
		    var chart = new google.visualization.ColumnChart(document.getElementById("column_tab4"));
		    chart.draw(data, options);
		    }
		    }
	    });
	},
	make_column_chart2:function(from_date,to_date){
	frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_jv_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));

			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		  	 console.log(r.message.order_total[0]);
		  	 for(var x in r.message.order_total){
  				mydata.push(r.message.order_total[x]);
               }
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Revenue Activities'
		    };
		    var chart = new google.visualization.ColumnChart(document.getElementById("column_tab2"));
		    chart.draw(data, options);
		  }
		}
	});
	},
	make_pie_chart2:function(from_date,to_date){
		    console.log("in the pie chart two");

			frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_jv_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));

			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		  	 console.log(r.message.order_total[0]);
		  	 for(var x in r.message.order_total){
  				mydata.push(r.message.order_total[x]);
               }
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Revenue Activities'
		    };
		    var chart = new google.visualization.PieChart(document.getElementById('pie_tab2'));
		    chart.draw(data, options);
		  }
		}
	});
	},
	make_column_chart4:function(from_date,to_date){
	frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_jv_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));

			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		  	 console.log(r.message.order_total[0]);
		  	 for(var x in r.message.order_total){
  				mydata.push(r.message.order_total[x]);
               }
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Revenue Activities'
		    };
		    var chart = new google.visualization.ColumnChart(document.getElementById("column_tab4"));
		    chart.draw(data, options);
		  }
		}
	});
	},
	make_pie_chart4:function(from_date,to_date){
		    console.log("in the pie chart two");

			frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_jv_data",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));

			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		  	 console.log(r.message.order_total);
		  	 console.log(r.message.order_total[0]);
		  	 for(var x in r.message.order_total){
  				mydata.push(r.message.order_total[x]);
               }
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Revenue Activities'
		    };
		    var chart = new google.visualization.PieChart(document.getElementById('pie_tab4'));
		    chart.draw(data, options);
		  }
		}
	});
	},
	make_column_chart5:function(from_date,to_date){
		console.log("in the column chart 5");
	frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_data_newsale",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));

			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['Year','Count']];
		  	 console.log("in the sales function");
		  	 for(var x in r.message.order_total){
  				mydata.push(r.message.order_total[x]);
               }
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Revenue Activities'
		    };
		    var chart = new google.visualization.ColumnChart(document.getElementById("column_tab5"));
		    chart.draw(data, options);
		  }
		}
	});
	},
	make_pie_chart5:function(from_date,to_date){
		    console.log("in the pie chart 5");

			frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_data_newsale",
			args: {
					from_date:from_date,
					to_date:to_date
				},
			callback: function(r) {
				console.log(typeof(r.message));

			var options = {packages: ['corechart'], callback : drawChart};
		    google.load('visualization', '1', options);
		    // google.setOnLoadCallback(drawChart);
		    function drawChart() {
		  	 mydata=[['sales','Expenses']];
		  	 console.log(r.message.order_total[0]);
		  	 for(var x in r.message.order_total){
  				mydata.push(r.message.order_total[x]);
               }
		    var data = google.visualization.arrayToDataTable(mydata);
		    var options = {
		      title: 'Revenue Activities'
		    };
		    var chart = new google.visualization.PieChart(document.getElementById('pie_tab5'));
		    chart.draw(data, options);
		  }
		}
	});
	},

	make_link: function(){
		var me = this;

    	this.country = this.wrapper.appframe.add_field({
			fieldname: "country",
			label: __("Country"),
			fieldtype: "Link",
			options: "Country"
		});

		
		this.from_date = this.wrapper.appframe.add_date(
			"From Date");

		
		this.to_date = this.wrapper.appframe.add_date(
			"To Date").change(function()
			 {	
			 	var from_date=me.from_date.val();
			 	var to_date=$(this).val();
			 	me.make_pie_chart(from_date,to_date)
				me.make_column_chart(from_date,to_date)
				
			 	});

		this.country = this.wrapper.appframe.add_field({
			fieldname: "currency",
			label: __("Currency"),
			fieldtype: "Link",
			options: "Currency"
		});
	
	
    },
	make_menu: function(){
		var me = this;

    	this.menu_field=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Link",
			"options": "Country",
			"label": "Country",
			"fieldname": "country",
			"placeholder": "Country"
	// "only_input":true
			},
		"only_input":true,
		parent:$(me.wrapper).find("#ctab"),
		});
		this.menu_field.make_input();
		$(this.wrapper).find("#ctab").css("width","200px");

		this.group_field1=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Date",
			"label": "From Date",
			"fieldname": "from_date",
			"placeholder": "From Date"
			},
		parent:$(me.wrapper).find("#ctab1"),
		});
		this.group_field1.make_input();
		 $(this.wrapper).find("#ctab1").css("width","200px");

		this.group_field2=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Date",
			"label": "To Date",
			"fieldname": "to_date",
			"placeholder": "To Date"
			},
		parent:$(me.wrapper).find("#ctab2"),
		});
		this.group_field2.make_input();
		$(this.wrapper).find("#ctab2").css("width","200px");

		this.menu_field=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Link",
			"options": "Currency",
			"label": "Currency",
			"fieldname": "Currency",
			"placeholder": "Currency"
	// "only_input":true
			},
		"only_input":true,
		parent:$(me.wrapper).find("#ctab3"),
		});
		this.menu_field.make_input();
		$(this.wrapper).find("#ctab3").css("width","200px");



         this.group_field2.$input.on("change", function() {
			    var from_date=me.group_field1.$input.val();
			 	var to_date=$(this).val();
			 	console.log(from_date);
			 	console.log(to_date);
			 	me.make_pie_chart2(from_date,to_date)
				me.make_column_chart2(from_date,to_date)
		});

	},
		make_menu2: function(){
		var me = this;

    	this.menu_field=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Link",
			"options": "Country",
			"label": "Country",
			"fieldname": "country",
			"placeholder": "Country"
	// "only_input":true
			},
		"only_input":true,
		parent:$(me.wrapper).find("#ctab22"),
		});
		this.menu_field.make_input();
		$(this.wrapper).find("#ctab").css("width","60%");

		this.group_field1=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Date",
			"label": "From Date",
			"fieldname": "from_date",
			"placeholder": "From Date"
			},
		parent:$(me.wrapper).find("#ctab122"),
		});
		this.group_field1.make_input();
		 $(this.wrapper).find("#ctab122").css("width","100%");

		this.group_field2=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Date",
			"label": "To Date",
			"fieldname": "to_date",
			"placeholder": "To Date"
			},
		parent:$(me.wrapper).find("#ctab222"),
		});
		this.group_field2.make_input();
		$(this.wrapper).find("#ctab22").css("width","100%");

		this.menu_field=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Link",
			"options": "Currency",
			"label": "Currency",
			"fieldname": "Currency",
			"placeholder": "Currency"
	// "only_input":true
			},
		"only_input":true,
		parent:$(me.wrapper).find("#ctab322"),
		});
		this.menu_field.make_input();
		$(this.wrapper).find("#ctab322").css("width","200px");

         this.group_field2.$input.on("change", function() {
			    var from_date=me.group_field1.$input.val();
			 	var to_date=$(this).val();
			 	console.log(from_date);
			 	console.log(to_date);
			 	me.make_pie_chart2(from_date,to_date)
				me.make_column_chart2(from_date,to_date)
		});

	},
	make_menu4: function(){
		var me = this;

    	this.menu_field=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Link",
			"options": "Country",
			"label": "Country",
			"fieldname": "country",
			"placeholder": "Country"
	// "only_input":true
			},
		"only_input":true,
		parent:$(me.wrapper).find("#ctab44"),
		});
		this.menu_field.make_input();
		$(this.wrapper).find("#ctab44").css("width","60%");

		this.group_field1=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Date",
			"label": "From Date",
			"fieldname": "from_date",
			"placeholder": "From Date"
			},
		parent:$(me.wrapper).find("#ctab144"),
		});
		this.group_field1.make_input();
		 $(this.wrapper).find("#ctab144").css("width","100%");

		this.group_field2=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Date",
			"label": "To Date",
			"fieldname": "to_date",
			"placeholder": "To Date"
			},
		parent:$(me.wrapper).find("#ctab244"),
		});
		this.group_field2.make_input();
		 $(this.wrapper).find("#ctab244").css("width","100%");

	    this.menu_field=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Link",
			"options": "Currency",
			"label": "Currency",
			"fieldname": "Currency",
			"placeholder": "Currency"
	// "only_input":true
			},
		"only_input":true,
		parent:$(me.wrapper).find("#ctab344"),
		});
		this.menu_field.make_input();
		$(this.wrapper).find("#ctab344").css("width","200px");

        this.group_field2.$input.on("change", function() {
			    var from_date=me.group_field1.$input.val();
			 	var to_date=$(this).val();
			 	console.log(from_date);
			 	console.log(to_date);
			 	me.make_pie_chart2(from_date,to_date)
				me.make_column_chart2(from_date,to_date)
		});

	},
		make_menu5: function(){
		var me = this;

    	this.menu_field=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Link",
			"options": "Country",
			"label": "Country",
			"fieldname": "country",
			"placeholder": "Country"
	// "only_input":true
			},
		"only_input":true,
		parent:$(me.wrapper).find("#ctab55"),
		});
		this.menu_field.make_input();
		$(this.wrapper).find("#ctab55").css("width","60%");

		this.group_field1=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Date",
			"label": "From Date",
			"fieldname": "from_date",
			"placeholder": "From Date"
			},
		parent:$(me.wrapper).find("#ctab155"),
		});
		this.group_field1.make_input();
		 $(this.wrapper).find("#ctab155").css("width","100%");

		this.group_field2=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Date",
			"label": "To Date",
			"fieldname": "to_date",
			"placeholder": "To Date"
			},
		parent:$(me.wrapper).find("#ctab255"),
		});
		this.group_field2.make_input();
		 $(this.wrapper).find("#ctab255").css("width","100%");

	    this.menu_field=frappe.ui.form.make_control({
		df: {
		    "fieldtype": "Link",
			"options": "Currency",
			"label": "Currency",
			"fieldname": "Currency",
			"placeholder": "Currency"
	// "only_input":true
			},
		"only_input":true,
		parent:$(me.wrapper).find("#ctab355"),
		});
		this.menu_field.make_input();
		$(this.wrapper).find("#ctab355").css("width","200px");

        this.group_field2.$input.on("change", function() {
			    var from_date=me.group_field1.$input.val();
			 	var to_date=$(this).val();
			 	console.log(from_date);
			 	console.log(to_date);
			 	me.make_pie_chart5(from_date,to_date)
				me.make_column_chart5(from_date,to_date)
		});

	},
	show_active_users: function() {
		var me = this;
		return frappe.call({
			method:"frappe.core.page.graphical_chart.graphical_chart.get_activities",
			callback: function(r,rt) {
				var $body = $(me.wrapper).find('.layout-side-section');
				$('<h4>Activities</h4><hr>\
				').appendTo($body);
				// r.message.sort(function(a, b) { return b.has_session - a.has_session; });
				console.log(r.message)
				for(var i in r.message) {
					console.log(r.message)

					var p = r.message[i];
					p.image = frappe.utils.get_file_link(frappe.user_info(p.name).image);
					$(repl('<p>\
						<span class="avatar avatar-small" \
							title="%(status)s"><img src="%(image)s" /></span>\
						<a>%(subject)s</a> @ <a>%(site_name)s</a>\
						</p>', p))
						.appendTo($body);
					// }
				}
			}
		});
	},


	
});


