
# Keep all your routes posted here
# 'REQUEST TYPE : ControllerNAme . function'
from api.controllers import TestController
from api.controllers import TodoController
methods = {

	'GET  /'	 :	TestController.test,

	'POST /todo'  : TodoController.add,

	'GET /todo/<id>' : TodoController.get,

	'DELETE /todo/<id>' : TodoController.delete,

	'GET /testdd/<int:t>'		: TodoController.test  

	#'GET /mongo' : TestController.mongoRecord
	

	}