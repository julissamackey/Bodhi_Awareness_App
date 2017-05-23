$(document).ready(function(){

	var sex =[];
	var stress=[];
	var tasks = [];
	var goals= [];
	var physCond =[];
	var cogCond = [];
	var sleep = [];
	var diet = [];
	var dietScore= [];
	var indulgences = [];
	var physActivity = [];
	var outlets = [];
	var columns = [["x"],["sexually active"],["stress level"],["tasks completed"],["goals completed"],["overall physical condition"],["overall cognitive condition"],["hours slept"],["diet"],["indulgences"],["physical activity"], ["outlets"]];

	$('.form').submit(function(e){
		// e.preventDefault();
		if ($("#email").val() == "" || $("#password").val() == ""){
			$('#alert').html("<strong>OOPS</strong> we need your information to continue");
			$('#alert').fadeIn().delay(3000).fadeOut();
		}else{
			localStorage.setItem("email",$("#email").val());
			localStorage.setItem("password",$("#password").val());
			var data = {
			email: localStorage.getItem("email"),
			password: localStorage.getItem("password")
			}
			$.ajax({
				url: "http://127.0.0.1:3000/log-in",
				type: "POST",
				data: JSON.stringify(data),
			    contentType: 'application/json',
				dataType: "json",
				success: function(result){
					if (result == false){
						$("#alert").html("<strong>OOPS</strong> we couldn't find anyone using that information. <strong>Please try again.</strong>")
						$("#alert").fadeIn().delay(3000);
						$(".form")[0].reset();
					}
					if (result["gender"] == "M" || result["gender"] == "N/A"){
						console.log("bravo macho o z");
						$(".form").hide();
						getSexHistory();
						}
					if (result["gender"] == "F"){
						console.log("bravo una dama");
						$(".form").hide();
						generateHerChart();
					}
				},
				error: function(xhr, ajaxOptions, thrownError){
					alert("OOPS... something went wrong. Check your internet connection.");
				}	
			});
		}
		return false;
	})
	var generateHerChart = function(){
		console.log("mujerona")
	}
	
	var generateChart = function(columns){
		console.log("hombre o que");
		console.log(columns);
		var chart = c3.generate({
			data: {
				x: 'x',
				columns:[
				columns[0],
				columns[2],
				columns[5],
				columns[6],
				columns[7]
				]
			},
			axis:{
				x:{
					type: "timeseries",
					tick: {
						format: "%Y-%m-%d"
					}
				}
			}
		})
	}

	var getSexHistory = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/sexual-activity?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					sex.push(result[x]);	
				}
				console.log(sex);
				for (var z = 0; z<sex.length; ++z){
					columns[0].push(sex[z].entry_date)
				}
				for (var s= 0; s<sex.length; ++s){
					columns[1].push(sex[s].active)
				}
				console.log(columns)
				getStressHistory();
			},
			error: function(xhr, ajaxOptions, thrownError){
				alert(xhr.status);
				alert(thrownError);
			}
		})
	}

	var getStressHistory = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/stress?email="+ localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					stress.push(result[x]);	
				}
				console.log(stress);
				for (var s= 0; s<stress.length; ++s){
					columns[2].push(stress[s].level)
				}
				console.log(columns)
				getTasks();
			},
			error: function(xhr, ajaxOptions, thrownError){
				alert(xhr.status);
				alert(thrownError);
			}
		})
	};

	var getTasks = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/tasks?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					tasks.push(result[x]);	
				}
				console.log(tasks);
				for (var l =0; l<tasks.length; ++l){
					columns[3].push(tasks[l].complete)
				}
				console.log(columns)
				getGoals();
			}
		})		
	}


	var getGoals = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/goals?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					goals.push(result[x]);	
				}
				console.log(goals);	
				for (var g = 0; g<goals.length;++g){
					columns[4].push(goals[g].complete)
				}
				console.log(columns)
				getPhysCond();			
			},
			error: function(xhr, ajaxOptions, thrownError){
				alert(xhr.status);
				alert(thrownError);
			}
		})
	}

	var getPhysCond = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/physical-cond?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					physCond.push(result[x]);	
				}
				console.log(physCond);
				for (var x=0; x<physCond.length; ++x ){
					columns[5].push(physCond[x].overall)
				}				
				console.log(columns)
				getCogCond();
			}
		})		
	} 

	var getCogCond = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/cog-cond?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					cogCond.push(result[x]);	
				}
				console.log(cogCond);				
				for (var c=0; c<cogCond.length; ++c){
					columns[6].push(cogCond[c].overall)
				}			
				console.log(columns)
				getSleep();
			}
		})		
	}

	var getSleep = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/sleep?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					sleep.push(result[x]);	
				}
				console.log(sleep);
				for (var s=0; s<sleep.length; ++ s){
					columns[7].push(sleep[s].hours)
				}				
				console.log(columns)
				// getDiet();
				generateChart(columns);	
			}
		})		
	}

	var getDiet= function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/diet?user="+localStorage.getItem("email"),
			success: function(result){
				var score; 
				for (var x = 0; x<result.length; ++x){
					diet.push(result[x]);	
				}
				console.log(diet);
				// for (var a= 0; a<diet.length; ++a){
				// 	var dailyPoints= [0];
				// 	for (var b= 0; b<diet[a].length; ++b){
				// 		if (diet[a][b] == true){
				// 			var tempScore= [0];
				// 			dailyPoints= tempScore + 3;
				// 		}
			}
		})		
	};

	var getIndulgences = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/indulgences?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					indulgences.push(result[x]);	
				}
				console.log(indulgences);				
			}
		})
	}

	var getPhysActivity = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/physical-activity?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					physActivity.push(result[x]);	
				}
				console.log(physActivity);				
			}
		})
	}

	var getOutlets = function(){
		$.ajax({
			method:"GET",
			url: "http://127.0.0.1:3000/outlets?user="+localStorage.getItem("email"),
			success: function(result){
				for (var x = 0; x<result.length; ++x){
					outlets.push(result[x]);	
				}
				console.log(outlets);				
			}
		})
	}		
})

