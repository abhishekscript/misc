import os ,json 
import sys
args = sys.argv[1:]
path = os.getcwd()
def confirmation(target):
	print target+" For The API Already exists. Override (Y/N) ?"
	reply = raw_input()
	if reply in ['n','N','No','no']:
		return False
	return True

def checkList():
	listLength = len(args)
	#print listLength#, self.args
	if listLength < 1:
		print "Usage :\npython generate.py -h api"
		print "python generate.py -h service"
	else:
			if args[0] == '-h':
				print 'python generate.py api api_name attr1 attr2\nexample: python generate user name age gender\n will create controller/model for user with attributes name age and gender'
			elif args[0] == 'api':
				print "Generating API's"
				#if len(args[1])
				args[1] = args[1].title()
				if os.path.isfile(path+'/api/controllers/'+args[1]+"Controller.py"):
					if confirmation("Controller"):
						createAPI("api/controllers/"+args[1]+"Controller.py")
				else:
					createAPI("api/controllers/"+args[1]+"Controller.py")

				if os.path.isfile(path+"/api/models/"+args[1]+".py"):
					if confirmation("Model"):
						createAPI("api/models/"+args[1]+".py")
				else:
					createAPI("api/models/"+args[1]+".py")

			else:
				print "Invalid Arguements Given"
def createAPI(targetType):
		content = ""
		with open(path+"/config/setupFileContent") as inputFile:
			for x in inputFile:
				content+=x
		#print targetType.find('api/models')
		if targetType.find('api/controllers')>=0:
			#print targetType
			content = content[ content.find("<controller>")+13 : content.find("</controller>")  ]		
			content = content.replace("{{Test}}", args[1].title())
			#print content	
		else:
			content = content[ content.find("<models>")+9 : content.find("</models>") ]
			content = content.replace("{{Test}}", args[1].title())
			if len(args[2:])>0:
				#print "Model attrs available"
				modelData = "{\n"
				for x in args[2:]:
					modelData+="\t\t\t\t'"+x+"':  { 'type' : str, 'strict' : True },\n"
				
				modelData+="\t\t\t}"
				content = content.replace("{{attributes}}", modelData )

			else:
				content = content.replace("{{attributes}}", "{\n\n}")
		#	print content
			#print content
		with open(path+"/"+targetType, 'w') as outfile:
			content = content.replace('{{Test}}',args[1])
			outfile.write(content)
		outfile.close()
		print "created ",targetType

checkList()
