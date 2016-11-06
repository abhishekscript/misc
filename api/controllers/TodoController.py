from api.models import Todo
from api.responses import  req, res

def add():
	if req.body('title') == None or req.body('text') == None:
		return res.badRequest( "Missing Parametes" )

	result = Todo.add( req.body() ) 
	if result is not None:
		return res.dump({ "message" : "successfully added" , "data" : result })

	return res.negotiate({"message"  : "something went wrong" })


def get( id ):
	result = Todo.get(id)
	return res.dump({ "message" : result } )

def delete( id ):
	result = Todo.delete(id)
	print result, "##"
	return res.dump({ "message" : result })

def test(t):
	print t
	#print Misc.debug("hello")
	return "ff"