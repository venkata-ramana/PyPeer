from Tkinter import *
root = Tk()                                                                                 #Creating obj for Tkinter
root.title("Peer to Peer List")                                                             #Title of root Window
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(350, 570))
root.config(bg='#143')
btn1=Button(root,text='Send',font=('FreeSerif',16),bg='#00ffa4',fg='#fff',width=12,height=1,highlightthickness=0,command=lambda (self):{


}
)
btn1.place(x=100,y=150)
btn2=Button(root,text='Recieve',font=('FreeSerif',16),bg='#00bcd4',fg='#fff',width=12,height=1,highlightthickness=0)
btn2.place(x=100,y=250)

root.mainloop()