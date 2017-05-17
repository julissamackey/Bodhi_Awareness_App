$(document).ready(function(){

	$('select').material_select();

	var firstName = "";
	var lastName = "";
	var email = "";
	var password = "";
	var gender = ""; 
	var baseURL = "http://127.0.0.1:3000/sign-up?"

	console.log('hello world - sign up page');
	
	$('.createAccount').submit(function(event){
		event.preventDefault();	
			firstName = document.getElementById('firstName').value;
			lastName = document.getElementById('lastName').value;
			email = document.getElementById('email').value;
			password = document.getElementById('password').value;
			var genderSelection = document.getElementById('gender');
			gender = genderSelection.value;	
		var formData = {
			firstName: firstName, 
			lastName: lastName,
			email: email,
			password: password,
			gender: gender
			}
		signUpAjax(formData)	
		})

	var signUpAjax = function(formData){
	
		  $.ajax({
		    method: "POST",
		    url:baseURL+'email='+email+'&password='+password+"&firstName="+firstName+"&lastName="+lastName+"&gender="+gender,
		    success: function(result){
		      console.log(result);
		    }
		  })
	}


})