from flask import *
from connections import *
import api.models as model
import logs
try:
	from bson.objectid import ObjectId
except:
	print "mongodb"
	pass


ucheck = type(u'')
scheck = type('')
def validate(data=None,  attribs=None):
	if data is None or  attribs is None:
		return False

	for x in attribs:
		if data.get(x,None) :
			typ = type(data[x])
			#print ucheck, attribs[x]['type'] , ucheck, scheck
			if typ == ucheck and attribs[x]['type'] == scheck:
				pass
			elif typ != attribs[x]['type']:
				return {"message" : "invalid type on "+x },False

		elif attribs[x]['strict']:
			return {"message" : "missing key "+x } , False
		else:
			if attribs[x].get('defaultsTo',None) is not None:
				data[x] = attribs[x]['defaultsTo']

	return data , True

def debug(data, tag=None, force=False ):
	print logs
	print data

def error(data, tag=None, force=False ):
	return "dd"

def warn(data, tag=None, force=False ):
	return "dd"