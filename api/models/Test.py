from config import Misc
modelAttributes = {

        'age':  { 'type' : str, 'strict' : True },
        'name':  { 'type' : int, 'strict' : True },
      }

TestTable = Misc.mongo['Test']

def add( data ):
  valid = Misc.validate( data, modelAttributes )
  if not valid['status']: return valid
  
  return "Request passed :)"
  