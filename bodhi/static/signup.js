$(document).ready(function(){

	$('select').material_select();

	var username = "";
	var password = "";
	var baseURL = "http://127.0.0.1:3000/"
	var logInEP = "sign-up?" //blank&password=blank 

	console.log('hello world - sign up page');
	
	$('.createAccount').submit(function(event){
		event.preventDefault();
		var firstName = document.getElementById('firstName').value;
		var lastName = document.getElementById('lastName').value;
		var email = document.getElementById('email').value;
		var password = document.getElementById('password').value;
		var genderSelection = document.getElementById('gender');
		var gender = genderSelection.value;
		console.log(username);
		console.log(password);
		console.log(firstName);
		console.log(lastName);
		console.log(gender);
		signUpAjax(baseURL+logInEP+'email='+email+'&password='+password+'&firstName='+firstName+'&lastName='+lastName+'&gender='+gender)
	})

	

	var signUpAjax = function(url){
		var xhr = new XMLHttpRequest();
		xhr.open('POST', url, true);
		xhr.onload = function(){
			if (xhr.status >= 200 && xhr.status < 400){
				var response = xhr.responseText;
				logInSuccess(response);	
			}else{
				logInFail(response);
			}
		};
		xhr.onerror = function(){
			console.log('eeerrrrrr')
		}
		xhr.send();
	}; 	

	var logInFail=function(res){
		console.log('user not found');
		$('.logIn').hide();
		$('.userNotFound').fadeIn(2000);
	}

	var logInSuccess=function(res){
		console.log('success!');
		$('.logIn').hide();
		$('.showUserStuff').fadeIn(2000);		
	}
})