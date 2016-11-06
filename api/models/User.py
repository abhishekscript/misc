from config import Misc

modelAttributes = {
				'email':  { 'type' : str, 'strict' : True },
				'name':  { 'type' : int, 'strict' : True },
				'password':  { 'type' : str, 'strict' : True },
				'status'	: { 'type' : str, 'strict' : False, 'defaultsTo' : True }
			}

UserTable = Misc.mongo['User']

def add( data ):
	data , valid = Misc.validate( data, modelAttributes )
	print data, valid
	if not valid:	return data
	
	return "hello world"
	
	