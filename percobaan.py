from tkinter import *
from tkinter import ttk #Buat mengakses combobox dan triveiw
import csv
from Structure import PriorityQueue as Data 


class Main:
    def __init__(self): #nafiz
        self.window = Tk()
        self.window.geometry('300x300')
        self.window.title('')

        self.LgFrame = Frame(self.window)
        self.LgFrame.pack(fill=BOTH)

        mLabel = Label(self.LgFrame, text='\nSELAMAT DATANG \nDI LAYANAN PENGIRIMAN PAKET\n', font=('Arial', 13, 'bold'))
        mLabel.pack(side=TOP) 

        #######################################################
        Fr1 = Frame(self.LgFrame)
        Fr1.pack(fill=X, pady=5)

        lbl1 = Label(Fr1, width=10, text='Username', font=('Helvetica', 12, 'bold'))
        lbl1.pack(side=LEFT, pady=7)

        self.uid = Entry(Fr1, font=('calibri', 12))
        self.uid.pack(side=LEFT, fill=X, pady=9)

        #######################################################
        Fr2 = Frame(self.LgFrame)
        Fr2.pack(fill=X, pady=5)

        lbl2 = Label(Fr2, width=10, text='Password', font=('Helvetica', 12, 'bold'))
        lbl2.pack(side=LEFT, pady=7)

        self.pwd = Entry(Fr2, font=('calibri', 12))
        self.pwd.pack(side=LEFT, fill=X, pady=9)

        #######################################################
        Fr3 = Frame(self.LgFrame) 
        Fr3.pack(fill=X, pady=5)

        btL = Button(Fr3, text='Login', command=self.Login)
        btL.pack(side=BOTTOM, pady=7)

        self.window.mainloop()

    def Login(self): #Nafiz
        self.login = []
        with open('login.csv') as file:
            fl = csv.reader(file)
            for i in fl:
                self.login.append(i)
        
        self.menu() if [str(self.uid.get()), str(self.pwd.get())] in self.login else self.not_log()

    def Add(self): #Faruq
        for item in self.tbl.get_children(): #buat menghapus setiap data di tabel
            self.tbl.delete(item)
        
        value = None 
        if self.layanan.get() == ' Layanan YES':
            value = int(self.jrk.get())//3

        elif self.layanan.get() == ' Layanan SS':
            value = int(self.jrk.get())//1.5

        elif self.layanan.get() == ' Layanan REG':
            value = int(self.jrk.get())
        
        elif self.layanan.get() == ' Layanan OKE':
            value = int(self.jrk.get())*2

        else:
            return

        self.data.insert([str(value), self.bar.get(), self.tgl.get(), self.krm.get(), self.trm.get(), int(self.jrk.get()), self.layanan.get()])
        
        with open ('database.csv', 'w') as file:
            fl = csv.writer(file)
            fl.writerows(self.data.queue)

        f = open("database.csv", "r")
        
        for index, line in enumerate(f): #buat menampilkan datanya ditabel tkinter nya #enumarte ini list kesatuan dipecah pecah
            temp = line.rstrip().split(',')
            if line != '\n':
                self.tbl.insert('', END, iid = index, text = temp[1], values = temp[2:])

    def not_log(self): #Faruq
        Fr4 = Frame(self.LgFrame)
        Fr4.pack(fill=X, pady=5)

        lbl3 = Label(Fr4, width=10, text='Username atau Password salah!', fg='red')
        lbl3.pack(side=BOTTOM, pady=7, fill=BOTH)

    def menu(self): #Reza
        self.data = Data() #buat menampung data dari db nya
        with open('database.csv') as file:
            fl = csv.reader(file)
            for i in fl:
                if i != []:
                    self.data.insert(i)

        self.LgFrame.destroy() #buat menghilangkan lgframe dari self get windows
        self.window.geometry('900x500') #uk windows tkinternya

        ##############################################
        mFrame = Frame(self.window) #frame menu label nya dan tabel button insert dan pop
        mFrame.pack(fill=BOTH)

        mFr1 = Frame(mFrame)
        mFr1.pack(fill=X, pady=5)

        mLbl1 = Label(mFr1, width=10, text='MENU', font=('Arial',12, 'bold'))
        mLbl1.pack(side=TOP, pady=7, fill=BOTH)

        ##############################################
        mFr2 = Frame(mFrame)
        mFr2.pack(fill=BOTH, pady=5)

        col = ('tanggal', 'pengirim', 'penerima', 'jarak', 'layanan') #header nya

        self.tbl = ttk.Treeview(mFr2,columns=col)
        self.tbl.pack()

        #mengatur text header
        self.tbl.heading('#0', text='Barang')
        self.tbl.heading('tanggal', text='Tanggal')
        self.tbl.heading('pengirim', text='Pengirim')
        self.tbl.heading('penerima', text='Penerima')
        self.tbl.heading('jarak', text='Jarak')
        self.tbl.heading('layanan', text='Layanan')

        ##############################################
        f = open("database.csv", "r")

        for index, line in enumerate(f): #dibuat list 
            temp = line.rstrip().split(',')
            if line != '\n':
                self.tbl.insert('', END, iid = index, text = temp[1], values = temp[2:]) #menampilkan data db ke tabel

        #######################################
        mFr8 = Frame(mFrame)
        mFr8.pack(fill=X, pady=5)

        btI = Button(mFr8, text='Insert', command=self.Insert)
        btI.pack()

        btP = Button(mFr8, text='Pop', command=self.popdata)
        btP.pack()

    def Insert(self):  #Reo
        ins = Tk()
        ins.title('')
        #######################################
        iFr1 = Frame(ins)
        iFr1.pack(fill=X, pady=5)

        ilbl2 = Label(iFr1, text='Barang\t\t')
        ilbl2.pack(side=LEFT)

        self.bar = Entry(iFr1)
        self.bar.pack(side=LEFT)

        #######################################
        iFr2 = Frame(ins)
        iFr2.pack(fill=X, pady=5)

        ilbl3 = Label(iFr2, text='Tanggal\t\t')
        ilbl3.pack(side=LEFT)

        self.tgl = Entry(iFr2)
        self.tgl.pack(side=LEFT)

        #######################################
        iFr3 = Frame(ins)
        iFr3.pack(fill=X, pady=5)

        ilbl4 = Label(iFr3, text='Pengirim\t')
        ilbl4.pack(side=LEFT)

        self.krm = Entry(iFr3)
        self.krm.pack(side=LEFT)

        #######################################
        iFr4 = Frame(ins)
        iFr4.pack(fill=X, pady=5)

        ilbl5 = Label(iFr4, text='Penerima\t')
        ilbl5.pack(side=LEFT)

        self.trm = Entry(iFr4)
        self.trm.pack(side=LEFT)
        
        #######################################
        iFr5 = Frame(ins)
        iFr5.pack(fill=X, pady=5)

        ilbl6 = Label(iFr5, text='Jarak\t\t')
        ilbl6.pack(side=LEFT)

        self.jrk = Entry(iFr5)
        self.jrk.pack(side=LEFT)

        ######################################
        iFr6 = Frame(ins)
        iFr6.pack(fill=X, pady=5)

        ilbl7 = Label(iFr6, text='Layanan\t\t')
        ilbl7.pack(side=LEFT)

        self.n = StringVar() 
        self.layanan = ttk.Combobox(iFr6, width = 17, textvariable = self.n)
        
        # Adding combobox drop down list
        # self.layanan['values'] = ('1', '2', '3', '4')
        self.layanan['values'] = (' Layanan YES', ' Layanan SS', ' Layanan REG', ' Layanan OKE')
        self.layanan.pack()
        self.layanan.current(2) #fungsi current ==> buat menampilkan value yang di  combobox , 2(reg)

        # iFr7 = Frame(ins).pack(fill=X, pady=5)
        
        # self.layanan = Entry(iFr7).pack(side=LEFT)
        #######################################
        iFr8 = Frame(ins)
        iFr8.pack(fill=X, pady=5)

        iBtn = Button(iFr8, text='Insert', command=self.Add)
        iBtn.pack()
        
        ins.mainloop()

    def popdata(self): #Reza
        # print(True)

        self.data.delete()

        with open('database.csv', 'w') as db:
            dbs = csv.writer(db)
            dbs.writerows(self.data.queue)

        for item in self.tbl.get_children(): #mengambil value ditabel
            self.tbl.delete(item)#menghapus data semua yang ada ditabel nya

        f = open("database.csv", "r")

        for index, line in enumerate(f):
            temp = line.rstrip().split(',') 
            if line != '\n':
                self.tbl.insert('', END, iid = index, text = temp[1], values = temp[2:])


if __name__ == '__main__':
    Main()