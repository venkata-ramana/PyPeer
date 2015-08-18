from Tkinter import *                                                                   #import Libraries
import ttk as tk
from PIL import Image, ImageTk, ImageFilter
from tkFileDialog import *
from tkMessageBox import *
from sqlite3 import *
import qrcode
import hashlib

class AddObjects(Canvas):

    def __init__(self,parent):
        self.addIcon = ImageTk.PhotoImage(Image.open("./icons/AddFiles22.png"))
        self.searchIcon = ImageTk.PhotoImage(Image.open("./icons/Search22.png"))
        self.alarmIcon = ImageTk.PhotoImage(Image.open("./icons/Alarm22.png"))
        self.timerIcon = ImageTk.PhotoImage(Image.open("./icons/Timer22.png"))
        self.settingIcon= ImageTk.PhotoImage(Image.open("./icons/Settings22.png"))
        self.closeIcon= ImageTk.PhotoImage(Image.open("./icons/close.png"))
        self.width = Canvas.winfo_reqwidth(parent)

    def add_entry(self,func=None):
        self.srchLabel=Label(root.mycanvas,background=bgHoverColor)
        self.srchLabel.place(x=(self.width-680), y=0, width=(self.width-350), height=60)

        self.logo=Label(self.srchLabel,background=bgHoverColor)
        self.logo.place(x=0,y=0,width=40,height=60)
        self.logo.config(image=self.searchIcon)

        self.entryBox = Entry(self.srchLabel,width=35,font=('calibri',10),highlightthickness=0,fg='#FFF')
        self.entryBox.place(x=40,y=18)
        self.entryBox.insert(0,'Search')
        self.entryBox.config(bg=bgHoverColor,bd=0)
        self.entryBox.bind('<Button-1>',lambda (parent):self.entryBox.delete(0,END))
        self.closebtn=Label(self.srchLabel,background=bgHoverColor,fg="#FFF",cursor="hand1")
        self.closebtn.config(image=self.closeIcon)
        self.closebtn.bind('<Button-1>',lambda (parent):self.srchLabel.destroy())
        self.closebtn.place(x=405,width=30,height=60)

    def addfolder(self,func=None):

        def choosedir(self):
            root.obj.directory.destroy()
            filename=askdirectory(parent=root)
            if filename:
                conn = connect('test.db')
                a=b=var=0
                data=conn.execute("INSERT INTO Peer_to_Peer VALUES(?,?,?,?)", (filename, a, b,var))
                conn.commit()
                conn.close()
                root.dataview.freeTable()
                root.dataview.LoadTable()
                var=var+1

        def choosedirfiles(self):
            root.obj.directory.destroy()
            filename=askopenfilenames(parent=root)
            if filename:
                conn = connect('test.db')
                a=b=var=0
                for i in filename:
                    data=conn.execute("INSERT INTO Peer_to_Peer VALUES(?,?,?,?)", (i, a, b,var))
                    conn.commit()
                    var=var+1

                conn.close()
                root.dataview.freeTable()
                root.dataview.LoadTable()

        self.directory=Toplevel(root)
        self.directory.title('Add Files/Folder')
        self.directory.resizable(width=False,height=False)
        self.dirCanvas=Canvas(self.directory,width=420, height=250, bg="#fff", highlightthickness=0)
        self.dirCanvas.pack(fill=BOTH, expand=YES)
        self.addfold=Label(self.dirCanvas,text='Add Folder',background=bgHoverColor,fg='#fff',cursor="hand1")
        self.addfold.place(x=50, y=50, width=150, height=150)
        self.addfold.bind('<Button-1>',choosedir)
        self.addfile=Label(self.dirCanvas,text='Add Files',background=bgHoverColor,fg='#fff',cursor="hand1")
        self.addfile.place(x=220, y=50, width=150, height=150)
        self.addfile.bind('<Button-1>',choosedirfiles)

        self.sendFiles = Label(root.mycanvas,background=bgHoverColor,text='Share All',fg='#FFF',cursor="hand1")
        self.sendFiles.place(x=150, y=10, width=150, height=40)
        self.sendFiles.bind("<Button-1>", self.shareFiles)

        self.clearFiles = Label(root.mycanvas,background=bgHoverColor,text='Clear All',fg='#FFF',cursor="hand1")
        self.clearFiles.place(x=320, y=10, width=150, height=40)
        self.clearFiles.bind("<Button-1>", lambda (self):{
                                                root.dataview.emptyTable(),
                                                root.dataview.freeTable(),
                                                root.dataview.LoadTable()
                                                    }
        )

    def showHistory(self,func=None):
        self.wind=Toplevel(root)
        self.wind.title('History')
        self.wind.resizable(width=False,height=False)
        self.topCanvas=Canvas(self.wind,width=500, height=500, bg="#fff", highlightthickness=0)
        self.topCanvas.pack(fill=BOTH, expand=YES)
        self.history=ShowHistoryWindow(self.topCanvas)
        self.history.LoadTable()
        self.history.bind("WM_DELETE_WINDOW", self.hideHistory)

    def hideHistory(self):
        self.history.freeTable()
        self.wind.destroy()

    def showSettings(self,func=None):
        self.settingsWindow=Toplevel(root)
        self.settingsWindow.title('Settings')
        self.settingsWindow.resizable(width=False,height=False)
        self.SettopCanvas=Canvas(self.settingsWindow,width=500, height=500, bg="#fff", highlightthickness=0)
        self.SettopCanvas.pack(fill=BOTH, expand=YES)

    def shareFiles(self,func=None):
        a = hashlib.sha224()
        hexacode=a.hexdigest()
        qr.add_data(hexacode)
        self.share=Toplevel(root)
        self.share.title('Manual Connection')
        self.share.resizable(width=False,height=False)
        self.shareCanvas=Canvas(self.share,width=800, height=300, bg="#fff", highlightthickness=0)
        self.shareCanvas.pack(fill=BOTH, expand=YES)
        qrpanel = Label(self.share, image =img,bg='#fff')
        qrpanel.place(x=20, y=20,width=200,height=200)
        orlabel = Label(self.share,text='(OR)',bg="#fff", highlightthickness=0)
        orlabel.place(x=260,y=100)
        codepanel = Entry(self.share, font=('calibri',8),bg='#fff')
        codepanel.place(x=350, y=80,width=400,height=30)
        codepanel.insert(0,hexacode)
        btnpanel = Button(self.share,text='Copy to ClipBoard',bg='#123',fg='#fff',width=15,height=2,cursor='hand1')
        btnpanel.place(x=450,y=110)

    def add_objects(self):
        self.addLabel = Label(root.mycanvas,background=bgColor,cursor="hand1")
        self.addLabel.place(x=0, y=0, width=70, height=60)
        self.addLabel.bind("<Button-1>", self.addfolder)
        self.addLabel.config(image=self.addIcon)
        self.addLabel.bind("<Enter>", lambda(parent): self.addLabel.config(background=bgHoverColor))
        self.addLabel.bind("<Leave>", lambda(parent): self.addLabel.config(background=bgColor))

        self.SrchLabel = Label(root.mycanvas,background=bgColor,cursor="hand1")
        self.SrchLabel.place(x=(self.width-310), y=0, width=70, height=60)
        self.SrchLabel.bind("<Button-1>", self.add_entry)
        self.SrchLabel.config(image=self.searchIcon)
        self.SrchLabel.bind("<Enter>", lambda(parent): self.SrchLabel.config(background=bgHoverColor))
        self.SrchLabel.bind("<Leave>", lambda(parent): self.SrchLabel.config(background=bgColor))

        self.AlmLabel= Label(root.mycanvas,background=bgColor,cursor="hand1")
        self.AlmLabel.place(x=(self.width-230), y=0, width=70, height=60)
        self.AlmLabel.config(image=self.alarmIcon)
        self.AlmLabel.bind("<Enter>", lambda(parent): self.AlmLabel.config(background=bgHoverColor))
        self.AlmLabel.bind("<Leave>", lambda(parent): self.AlmLabel.config(background=bgColor))

        self.timLabel = Label(root.mycanvas,background=bgColor,cursor="hand1")
        self.timLabel.place(x=(self.width-150), y=0, width=70, height=60)
        self.timLabel.config(image=self.timerIcon)
        self.timLabel.bind('<Button-1>',self.showHistory)
        self.timLabel.bind("<Enter>", lambda(parent): self.timLabel.config(background=bgHoverColor))
        self.timLabel.bind("<Leave>", lambda(parent): self.timLabel.config(background=bgColor))

        self.SetLabel = Label(root.mycanvas,background=bgColor,cursor="hand1")
        self.SetLabel.place(x=(self.width-70), y=0, width=70, height=60)
        self.SetLabel.config(image=self.settingIcon)
        self.SetLabel.bind('<Button-1>',self.showSettings)
        self.SetLabel.bind("<Enter>", lambda(parent): self.SetLabel.config(background=bgHoverColor))
        self.SetLabel.bind("<Leave>", lambda(parent): self.SetLabel.config(background=bgColor))

class ShowHistoryWindow(Canvas):

    def __init__(self, parent):
        Canvas.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = tk.Treeview(self)
        tv['columns'] = ('Time', 'Status')
        tv.heading("#0", text='Name / Location', anchor='center')
        tv.column("#0", anchor="center",width=200)
        tv.heading('Status', text='Status')
        tv.column('Status', anchor='center', width=200)
        tv.heading('Time', text='Time')
        tv.column('Time', anchor='center', width=100)

        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        conn = connect('test.db')
        data=conn.execute("SELECT * from Peer_History")
        for row in data:
            self.treeview.insert('', 'end', text=row[1],values=(row[2],row[3]))

        conn.close()

    def freeTable(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def emptyTable(self):
        conn = connect('test.db')
        data=conn.execute("DELETE FROM Peer_History")
        conn.commit()
        conn.close()

class App(Canvas):

    def __init__(self, parent):
        Canvas.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = tk.Treeview(self,height=20)
        style = tk.Style()
        style.theme_settings("default", {"Treeview": {
       "configure": {"padding": 0},
       "map": {
           "background": [("active", "green2"),
                          ("!disabled", "green4")],
           "fieldbackground": [("!disabled", "#fff")
                               ],
           "foreground": [("focus", "#fff"),
                          ("!disabled", "OliveDrab2") ]
                }
    	    }
        })

        tv['columns'] = ('Status', 'Peers')
        tv.heading("#0", text='Name / Location', anchor='center')
        tv.column("#0", anchor="center",width=400)
        tv.heading('Status', text='Status')
        tv.column('Status', anchor='center', width=100)
        tv.heading('Peers', text='Peers')
        tv.column('Peers', anchor='center', width=150)
        tv.heading('Status', text='Status')
        tv.tag_configure('ttk',background='yellow')
        ysb = Scrollbar(orient=VERTICAL, command= tv.yview)
        tv['yscroll'] = ysb.set
        tv.grid(sticky=NSEW )
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):

        conn = connect('test.db')
        data=conn.execute("SELECT * from Peer_to_Peer")
        #self.closebtn.config(image=self.closeIcon)
        #width=750
        #height=18

        #print count
        #self.loadList(count)
        for row in data:
            #self.closeIcon= ImageTk.PhotoImage(Image.open("./icons/close15.png"))
            #self.sharebtn=Label(self.treeview,text='Share | ',bg=bgColor,fg='#fff',width=7,cursor='hand1')
            #self.sharebtn.bind('<Button-1>',lambda (parent):showinfo('Sharing','Path : %s'%row[0]))
            #self.closebtn=Label(self.treeview,text='x',bg=bgColor,fg='#fff',width=1,cursor='hand1')
            #self.closebtn.bind('<Button-1>',lambda (parent):{self.deleteChild('I00%d'%row[3],row[3]),self.loadList(len(self.token))})
            self.treeview.insert('', 'end', text=row[0], values=('%d'%row[1] +' Peers','%d'%row[2] + ' of '+'10' ))#,self.sharebtn.place(x=width-60,y=height),self.closebtn.place(x=width,y=height)))
            #height=height+20


        conn.close()

    def loadList(self,count):
        self.token=[]
        for i in range(count):
            self.token.insert(i,'I00%d'%i)

    def deleteChild(self,id,param):
        for i in self.treeview.get_children():
            if i==id:
                self.treeview.delete(id)
                self.removeChildFromDB(param)
                #self.sharebtn.destroy()
                #self.closebtn.destroy()
            else:
                print i,id

    def removeChildFromDB(self,param):
        conn = connect('test.db')
        data=conn.execute("DELETE FROM Peer_to_Peer WHERE `id`=%s"%param)
        conn.commit()
        conn.close()

    def freeTable(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
            #self.sharebtn.destroy()
            #self.closebtn.destroy()

    def emptyTable(self):
        conn = connect('test.db')
        data=conn.execute("DELETE FROM Peer_to_Peer")
        conn.commit()
        conn.close()

def callback():
    if askokcancel("Quit", "Do you really wish to quit?"):
        root.dataview.emptyTable()
        root.destroy()

class ShareFiles(Frame):
    def __init__(self):
        root.mycanvas = Canvas(topframe,width=820, height=60, bg="#fff", highlightthickness=0)           #Creating Canvas on Frame
        root.mycanvas.pack(fill=BOTH, expand=YES)
        root.mycanvas.create_rectangle(0, 0, 790, 60, fill=bgColor,outline=bgColor)                  #Header Bar
        root.obj=AddObjects(root.mycanvas)                                                                    #Objects on Header Bar
        root.obj.add_objects()

        root.centerCanavas = Canvas(topframe,width=790, height=1000, bg="#fff", highlightthickness=0)    #Body of the window
        root.centerCanavas.pack(fill=BOTH, expand=YES)
        root.dataview = App(root.centerCanavas)

root = Tk()                                                                                 #Creating obj for Tkinter
root.title("Peer to Peer List")                                                             #Title of root Window
root.resizable(width=False, height=False)                                                   #Disable Resizable option
root.protocol("WM_DELETE_WINDOW", callback)                                                 #Triggers when root window close
bgColor="#0097a7"            #607d8b
bgHoverColor="#00bcd4"       #779AAB
topframe = Frame(root)                                                                      #Creating Frame on root window
topframe.pack(fill=BOTH, expand=YES)
ShareFiles()
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=8,border=2)
qr.make(fit=True)
img = qr.make_image()
img = ImageTk.PhotoImage(img)
root.mainloop()

