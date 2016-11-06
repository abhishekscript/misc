from flask import Flask, Blueprint #,g
from config import connections,routes
from api.controllers import TestController
import sys
app = Flask(__name__)
#print g

#bp = Blueprint('frontend',TestController)
#app.register_blueprint(TestController.simple_page)
def processRoutes():
	routeCollection = routes.methods
	for k in routeCollection:
		print routeCollection[k]
		#main_view_func = Main.as_view(routeCollection[k])
		print(k)
		app.add_url_rule(k[ k.find("/") : ], endpoint=str(routeCollection[k]), view_func=routeCollection[k],methods=[ k[ 0 : k.find(" ")] ])
if __name__ == '__main__':
	processRoutes()
	app.run()