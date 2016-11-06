from flask import request,jsonify

def body(key=None):
	if key:
		return request.json.get(key,None)
	return request.json

def form(key):
	if key:
		return request.form.get(key,None)
	return request.form
	
def file(key):
	if key:
		return request.file.get(key, None)
	return request.file