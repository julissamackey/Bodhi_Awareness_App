$(document).ready(function(){

	$('div.quote').fadeIn(2000);	
	
	$('select').material_select();
	
	var username = "";
	var password = "";
	var baseURL = "http://127.0.0.1:3000/"
	var logInEP = "log-in?" //blank&password=blank 

	console.log('hello world');

	$('.logIn').submit(function(event){
		event.preventDefault();
		username = document.getElementById('existingUserEmail').value;
		password = document.getElementById('existingUserPassword').value;
		console.log(username);
		console.log(password);
		logInAjax(baseURL+logInEP+username+'&password='+password)
	})	

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

	var logInAjax = function(url){
		var xhr = new XMLHttpRequest();
		xhr.open('GET', url, true);
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