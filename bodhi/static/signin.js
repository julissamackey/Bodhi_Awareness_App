$(document).ready(function(){

	var username = "";
	var password = "";
	var baseURL = "http://127.0.0.1:3000/"
	var logInEP = "log-in?user=" //blank&password=blank 

	console.log('hello world');

	$('.logIn').submit(function(event){
		event.preventDefault();
		username = document.getElementById('existingUserEmail').value;
		password = document.getElementById('existingUserPassword').value;
		console.log(username);
		console.log(password);
		logInAjax(baseURL+logInEP+username+'&password='+password)
	})	
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