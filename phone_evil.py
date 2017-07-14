import xmlrpc.client

server1 = 'http://www.pythonchallenge.com/pc/phonebook.php'
server2 = 'http://www.pythonchallenge.com/pc/stuff/violin.php'

remote_server = xmlrpc.client.ServerProxy(server2)

server_answer = remote_server.system.listMethods()
print(server_answer)
server_answer = remote_server.system.methodSignature('phone')
print(server_answer)
server_answer = remote_server.system.methodHelp('system.listMethods')
print(server_answer)
server_answer = remote_server.system.methodHelp('phone')
print(server_answer)

server_answer = remote_server.phone('Leopold')
print(server_answer)

