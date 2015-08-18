import socket, sys
FRAME_SIZE = 9216
s = socket.socket()
s.bind(("localhost", 19999))
s.listen(10)
sc, address = s.accept()

i = t = 0
p = 1
list = ["/media/venkat/Education//Entertainment/3_Idiots_2009.mp4"]

for add in list:
    file = add.split('/')
    filename = file[len(file)-1]
    f= open(add, "rb")
    sc.send(filename)                            #send name of the file
    FILE_SIZE = 1547499624
    TIMER = 3167
    PERC = ((FILE_SIZE / FRAME_SIZE)/100)+1
    #sc.send(FILE_SIZE)                           #send size of the file
    l = f.read(FRAME_SIZE)

    while (l):
        if(i%TIMER==0):
            t+=1

        if(i%PERC==0):
            print "Percentage : "+str(p)+"%"
            p+=1

        sc.send(l)
        l = f.read(FRAME_SIZE)
        i+=1

sc.close()
s.close()
print "File transfer has completed"
print "Time Elapsed: "+str(t)+" Seconds"
print "Total Frames Needed : "+str(i)
