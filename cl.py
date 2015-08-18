import socket, sys, os

FRAME_SIZE = 9216
s = socket.socket()
s.connect(("localhost",19999))
name = s.recv(FRAME_SIZE)                                                          #recv name of the file

if not os.path.exists('/home/'+socket.gethostname()+'/Documents/Peer2Peer'):
    os.mkdir('/home/'+socket.gethostname()+'/Documents/Peer2Peer')

add = '/home/'+socket.gethostname()+'/Documents/Peer2Peer/'+name
i = t = 0
p = 1
FILE_SIZE = 1547499624 #int(s.recv(FRAME_SIZE))                                   #recv size of the file
TIMER = 3167
PERC = ((FILE_SIZE / FRAME_SIZE)/100)+1

f = open(add,'wb')                                                                  #open in binary
l = s.recv(FRAME_SIZE)
while (l):
    if(i%TIMER==0):
        t+=1

    if(i%PERC==0):
        print "Percentage : "+str(p)+"%"
        p+=1

    f.write(l)
    l = s.recv(FRAME_SIZE)
    i+=1

f.close()
s.close()

if(p>95):
    print "File transfer has completed"

print "Time Elapsed: "+str(t)+" Seconds"
print "Total Frames Needed : "+str(i)