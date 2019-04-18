import socket, threading
import time
from _thread import start_new_thread

def accept_client():
    while True:
        #accept new connection   
        cli_sock, cli_add = ser_sock.accept()
        uname = cli_sock.recv(1024)
        user.append((uname, cli_sock))
       
        wating_m.append((cli_sock,( "Chat room > {} has joined the chat room".format(uname.decode())).encode()))
        print('{} is now connected ip:- {}   port:- {} ' .format(uname.decode(), cli_add[0],cli_add[1]))
        start_new_thread(rec,(uname, cli_sock)) # making dedecated thread

#using dedecated thread
def rec(name,u):
   while True:
       try:
           data = u.recv(1024)
           if data:
               wating_m.append((u,("{} > {}".format( name.decode(),data.decode())).encode()))
       except Exception as x:
           print(name.decode()+' left chat room')
           wating_m.append((u,( "Chat room > {} has left the chat room".format(name.decode())).encode()))    
           try:
               user.remove((name,u))
           except:
               print('exception in removing')
           finally:
               break
               pass
    
   print("out")               










#prev code working with one thread
'''def broadcast_usr():
    while True:
        for i in user:
            try:
                data = i[1].recv(1024)
                if data:
                    wating_m.append((i[1],("{} > {}".format( i[0].decode(),data.decode())).encode()))
            except Exception as x:
                print(i[0].decode()+' left chat room')
                wating_m.append((i[1],( "Chat room > {} has left the chat room".format(i[0].decode())).encode()))
                
                try:
                    user.remove(i)
                except:
                    print('exception in removing')
                    pass
                continue'''
                
#using one thread to send meaasge to all person
def send():
    while True:
        if len(wating_m)>0:
            for i in user:
                try:
                    if (i[1] != wating_m[0][0]):
                        i[1].send(wating_m[0][1])
                       
                except Exception as x:
                        print((i[0]).decode()+' left chat room from send')
                        wating_m.append((i[1],( "Chat room > {} has left the chat room".format(i[0].decode())).encode()))
                       
                        try:
                            user.remove(i)
                        except:
                            print('exception in removing')
                            pass
                        continue
                        
            wating_m.remove(wating_m[0])
        

if __name__ == "__main__":    
    user = []
    wating_m=[]

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 5023
    ser_sock.bind((HOST, PORT))

    # listen    
    ser_sock.listen(10)
    print('Chat server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target = accept_client)
    thread_ac.start()

   
    thread_bsp = threading.Thread(target = send)
    thread_bsp.start()
    #thread_bs = threading.Thread(target = broadcast_usr) -----code of single thread
    #thread_bs.start()  -----code of single thread
    time.sleep(100000) #sever stays on for this amount of time
