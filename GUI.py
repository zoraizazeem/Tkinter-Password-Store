from tkinter import *
from numpy import *
from tkinter import ttk
import pandas as pd
import csv
from NewEncryptor import decryption
from NewEncryptor import encryption

data = pd.read_csv("Passwords.csv")
root = Tk()
storeTable = []

class Window(Frame) :

    def __init__(self, master=None) :
        Frame.__init__(self, master)
        self.master = master
        self.init_window

    @property
    def init_window(self) :
        self.master.title("Main Frame")
        self.pack(fill=BOTH, expand=1)
        self.configure(bg='#32CF00')

        quitbutton = Button(self, text="Quit", bg='green', fg='white', command=self.clint_exit)
        quitbutton.place(x=250, y=150)  # adjust the number of pixels of button
        
        NewPassBtn = Button(self, text="Add a new password", command=self.StorePassword)

        PassDirBtn = Button(self, text="View password directory", command=self.SeePassword)
        
        EnterButton = Button(self,text="Enter", bg='green', fg='white',  command=lambda : Unlock(nameEntered.get()))
        EnterButton.place(x=110, y=150)
        
        nameEntered = Entry(self, width=20, font = 50)
        nameEntered.config(bd=10)
        nameEntered.place(x=110, y=100)

        RetryBtn = Button(self, text= "OK ill retry!!",bg='red', fg='white', command=lambda : retryfunc(self))

        canvas = Canvas(self, width=390, height=300)

        img1 = PhotoImage(file="trashjpg.png")

        def retryfunc(self):
            canvas.place_forget()
            RetryBtn.place_forget()

        def Unlock(Passw):
            if str(Passw) == "Zoraiz":
                return PassDirBtn.place(x=200, y=200),  NewPassBtn.place(x=300, y=300)
            else:
                RetryBtn.place(x=450, y=250)
                canvas.place(x=50, y=200)
                canvas.create_image(20, 20, anchor=NW, image=img1)
                mainloop()
                #button5.place(x=450, y=450)


    def clint_exit(self) :
        exit()

############################################################################################
    def SeePassword(self):
        root2 = Toplevel()
        root2.title('The Vault')

        background_image = PhotoImage(file='vault-door-bank-with-lot-money_161488-314.png')
        bg_label = Label(root2, image = background_image)
        bg_label.place(x=1,y=1)

        #data2 = data['Accounts'].drop(:)
        comboAccount = ttk.Combobox(root2, values=data['Account'].tolist())
        comboAccount.place(x=250, y=150)
        SeePassBtn = Button(root2, text= "See password",bg='red', fg='Black', command=lambda : getpassword(comboAccount.current()))
        SeePassBtn.place(x=100, y=100)

        root2.geometry("600x350")

        f = open('PassStore.csv', 'r')
        with f:
            reader = csv.reader(f)
            for row in reader:
                storeTable.append(row)
        print(storeTable)

        def getpassword(k) :
            temp = data['Passwords']

            milk = (decryption((temp.loc[k]).split(" ")))

            passwordlabel = Label(root2, text= milk)
            passwordlabel.place(x=10, y=100)

        root2.mainloop()



################################################################################################
    def StorePassword(self):
        root3 = Toplevel()

        colnames = ['Accounts', 'Passwords']
        def addPass(Acc, Passw):
            encryptPass = encryption(Passw)
            copyLabel = Text(root3, height=10, width = 60)
            copyLabel.place(x=110, y=150)
            copyLabel.insert(1.0, "PLease copy this to the csv file where the encrypted passwords are kept: \n \n \n {},{}".format(Acc, encryptPass))
            '''with open('PassStore.csv', 'w') as f:
                writer = csv.DictWriter(f, fieldnames = colnames)
                writer.writeheader()
                writer.writerow({'Accounts' : '{}'.format(Acc), 'Passwords' : '{}'.format(Passw)})'''

        
        root3.title('Deposit')
        root3.geometry("400x400")

        root3.configure(background = "green")
       
        bg_label2 = Label(root3)
        bg_label2.pack()

        AccountEnt = Entry(root3, width=20, font = 50)
        PassEnt = Entry(root3, width=20, font = 50)
        #AccountEnt.config(bd=10)
        AccountEnt.place(x=110, y=100)
        PassEnt.place(x=110, y=300)

        EnterBtn = Button(root3, text= "Add password",bg='red', fg='Black', command=lambda : addPass(AccountEnt.get(), PassEnt.get()))
        EnterBtn.place(x=100, y=400)

        root3.mainloop()
##################################################################################################

root.geometry("550x550")

app = Window(root)
root.mainloop()
