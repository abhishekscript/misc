from pymongo import MongoClient
database = {
	
	'MongoDB' : {
		'host' 		: 'localhost',
		'port' 		: '27100',
		'database'	: 'misc'
		#'user' 		: 'user',
		#'password' 	: 'password',

	}

}

# SETTINGS FOR ABOVE CONFIGURATIONS
 
mongo = MongoClient()[database['MongoDB']['database']]#.database['database']
print mongo

