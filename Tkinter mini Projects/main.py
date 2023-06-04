from tkinter import *
from tkinter import messagebox 
from pandas import read_csv
class App(Tk):
    def __init__(self):
        super().__init__()

        
        self.beauty()

    def beauty(self):
        self.title('Login')
        self.geometry('400x400+450+100')
        self.configure(background='#61a2f2')
        self.lbl = Label(text='Login Please' , font = 'arial 20 bold' , background='#61a2f2')
        self.lbl.place(x = 50,y=40)
        self.username = StringVar()
        self.password = StringVar()

        self.frame = Frame(self, background='#61a2f2')
        self.frame.place(x = 100 ,y = 130)
        Label(self.frame , background='#61a2f2').pack()
        Label(self.frame , text = 'username' , background='#61a2f2').place(x=0 ,y=0)
        userentry = Entry(self.frame , textvariable=self.username , font = 'ariel 15' , borderwidth=0)
        userentry.pack()

        
        passentry = Entry(self.frame,textvariable=self.password , font = 'ariel 15' , borderwidth=0)

        Label(self.frame , background='#61a2f2').pack()
        Label(self.frame , background='#61a2f2' , text ='password').place(x=0 , y=75)
        self.lbl2 = Label(self.frame , background='#61a2f2' , text='' )
        self.lbl2.pack(expand=True)
        passentry.pack()
        

        self.lbl3 = Label(self.frame , background='#61a2f2' , text='',font = 'arial 10 ')
        self.lbl3.pack(expand=True)
        self.btn = Button(self.frame,text = 'Login' ,
             cursor='plus' , font = 'fantasy 13',
             padx=20 , borderwidth=0 , background='light green' , command = self.login)
        self.btn.pack()

    def login(self):
        self.user = self.username.get()
        self.pas  = self.password.get()

        self.df = read_csv('file.csv')
        user = self.df['username'].tolist()
        pw   = self.df['password'].tolist()

        self.user_index = 0
        self.password_index = 1

        if (self.user in user):
            self.user_index = user.index(self.user)
        if (self.pas in pw):
            self.password_index = pw.index(self.pas)
            

        if self.user_index == self.password_index:
            print(self.user_index , self.password_index)
            self.newpage()  
        elif  self.user_index != self.password_index:
            messagebox.showerror('Failed','Unvalid username or password')

        
               
    def newpage(self):
       self.frame.destroy()
       self.lbl.destroy()
       self.lbl2.destroy()

       self.data_page()
    
    def se_beauty(self):
        self.tit.destroy()
        self.frame.destroy()
        self.back_btn.destroy()
        self.beauty()
    
    def data_page(self):
        self.geometry('700x500+250+100')
        dt = self.df.iloc[self.user_index]
        self.name = dt['Name']
        self.age  = dt['Age']
        self.gender = dt['Gender']
        self.adress = dt['Adress']

        self.tit = Label(self , text = 'Hello........ '+self.name , font = 'italic 19 bold',
                         background='#61a2f2')
        self.tit.place(x= 200 , y = 80)
        self.frame = LabelFrame(self , text = 'Detail' , background='#61a2f2')
        self.frame.place(x = 180 , y = 200)

       
        self.name_lbl = Label(self.frame , text =  'Name   :   ' + self.name ,    font = 'comicsansms 19' , background='#61a2f2')
        self.age_lbl = Label(self.frame , text =   'Age    :   ' + str(self.age)    ,font = 'comicsansms 19', background='#61a2f2')
        self.gender_lbl = Label(self.frame , text ='gender :   ' + self.gender,font = 'comicsansms 19', background='#61a2f2')
        self.adress_lbl = Label(self.frame , text ='Adress :   ' + self.adress,font = 'comicsansms 19', background='#61a2f2')

        self.name_lbl.pack()
        self.age_lbl.pack()
        self.gender_lbl.pack()
        self.adress_lbl.pack()

        self.back_btn = Button(self ,text = '<--' , background='gray' , command = self.se_beauty , activeforeground='red')
        self.back_btn.place(x = 0 ,y =0)

           
if __name__ == "__main__":
    app = App()
    app.mainloop()
