import socket
from Tkinter import *


# object for TK
class Create_Messanger():
    def __init__(self):
        self.root = Tk()
        self.root.title('Server')
        self.root.resizable(width=False, height=False)
        self.root.geometry('{}x{}'.format(768,500))
        self.messages=Text(self.root, width=110, height=28, bg='#ddd')
        self.messages.place(x=0, y=0)
        #self.text = Entry(self.root,width=90,font=('Liberation Serif',12))
        #self.text .place(x=0, y=430)
        #self.btn = Label(self.root, font=('Liberation Serif',12), text='Send', bg='#fff', width=5 ,height=4,cursor='hand1')
        #self.btn.bind('<Button-1>', lambda (parent): self.send_message())
        #self.btn .place(x=725, y=432)
        self.root.mainloop()

    def send_message(self):
        msg = self.text.get()
        sc.send(msg)
        self.messages.mark_set("sentinel", INSERT)
        self.messages.mark_gravity("sentinel", RIGHT)
        self.messages.insert(END, msg+'\n')
        self.text.delete(0,END)
        self.text.focus_set()

    def show_message(self,msg):
        self.messages.insert(END,'> '+msg+'\n')

    def delete_message(self):
        self.messages.delete(0,END)


s = socket.socket()
s.bind(("localhost", 19999))
s.listen(1)
sc, address = s.accept()

obj=Create_Messanger()
abc=sc.recv(1024)
obj.show_message(abc)
sc.close()
s.close()