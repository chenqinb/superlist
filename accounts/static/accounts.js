var initialize = function(navigator, user, token, urls){
	console.log(navigator);
	$("#id_login").on("click", function(){
		navigator.id.request();
	});
	navigator.id.watch({
		loggedInUser: user,
		onlogin:function(assertion){
			$.post(
				urls.login, 
				{assertion:assertion, csrfmiddlewaretoken:token}
			)
				.done(function(){window.localtion.reload();})
				.fail(function(){navigator.id.logout();});
		
		},
		onlogout:function(){
		}
	});
};
window.Superlists = {
	Accounts: {
		initialize: initialize
	}
};
