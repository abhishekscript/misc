function init(){
	var left =  '<div class="list-group">'+
                '<a href="intro.html" class="list-group-item">Introduction</a>'+
                '<a href="hello.html" class="list-group-item">Hello World App</a>'+
                '<a href="controllers.html"class="list-group-item">Controllers</a>'+
                '<a href="models.html" class="list-group-item">Models</a>'+
                '<a href="database.html" class="list-group-item">Database</a>'+               
                '<a href="api.html" class="list-group-item">API </a>'+
          		'</div>';
    //document.getElementById('').innerHTML=left;
    document.getElementById("left_menu").innerHTML = left;
    var topBar =  '<div class="container-fluid">'+
				    '<div class="navbar-header">'+
				      '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">'+
				       '<span class="sr-only">Toggle navigation</span>'+
				        '<span class="icon-bar"></span>'+
				        '<span class="icon-bar"></span>'+
				        '<span class="icon-bar"></span>'+
				      '</button>'+
				      '<a class="navbar-brand" href="#">Misc.py</a>'+
				    '</div>'+

				    '<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">'+
				      
				      
				        '<ul class="nav navbar-nav navbar-right">'+
				          '<li><a href="#">Home</a></li>'+
				        '</ul>'+
				      '</div>'+
				    '</div>';
	var elem = document.getElementById('navBar');
	elem.innerHTML = topBar;
	elem.style.background = "#222";
}
init();