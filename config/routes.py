
# Keep all your routes posted here
# 'REQUEST TYPE : ControllerNAme . function'
from api.controllers import TestController
methods = {

	'GET  /'	 :	TestController.test,

	'GET /hello' :  TestController.hello

	#'GET /mongo' : TestController.mongoRecord
	

	}