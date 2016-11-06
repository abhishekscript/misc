from api.models import User
from api.responses import  req, res

def add():
	return  res.send( User.add( req.body() ) )