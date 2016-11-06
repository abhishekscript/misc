from config import Misc
modelAttributes = {
				'title':  { 'type' : str, 'strict' : True },
				'text':  { 'type' : str, 'strict' : True },
			}

TodoTable = Misc.mongo['Todo']

def add( data ):
	todo_id = TodoTable.insert( data )
	return todo_id

def get( id ):
	return TodoTable.find_one({ "_id" : Misc.ObjectId( id )  })

def delete( id ):
	action = TodoTable.delete_one({ "_id" : Misc.ObjectId( id ) })
	print vars(action)['_WriteResult__acknowledged']
	print action
	if action is not None:
		return "deleted"
	return "err deleting"

