import xmlrpclib

remote_server = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

server_answer = remote_server.system.listMethods()
print server_answer
server_answer = remote_server.system.methodSignature('phone')
print server_answer
server_answer = remote_server.system.methodHelp('system.listMethods')
print server_answer
server_answer = remote_server.system.methodHelp('phone')
print server_answer

server_answer = remote_server.phone('Bert')
print server_answer

