from flask import  jsonify, Response, render_template
from bson import json_util
import json
js , arr = type({}) , type([])
def badRequest(data=None):
	return jsonify({ "message" : data }), 400

def badRequestView(data=None):
	return render_template("404.html",message = data)

def negotiate(data=None, status=500):
	if data:
		if type(data) in [js,arr]:
			return jsonify(data),status
		return str(data),status	
	return jsonify({ message : data }), status

def dump(data):
	return Response(json_util.dumps(data), mimetype='application/json')

def send(data=None):
	if data:
		if type(data) in [js,arr]:
			return jsonify(data)
		return str(data)
	return jsonify({ message : data }), 404

	#return json.dumps(data, default =json_util.default)
	#return "1"
	#return Response( json_util.dumps(data) , mimetype='application/json' )