#Login App
from tkinter import *

class loginapp:
    global username,password
    username=["atiya","shubhadeep sir","zaheen bhaiya","ryan","tahmid bhaiya"]
    password=[1234,2345,3456,4567,5678]
    
    def login(self):
        
        self.screen=Tk()
        self.screen.title("my login app")
        self.screen.config(bg="Aquamarine")
        self.screen.geometry("500x500")
        
        self.userlabel=Label(self.screen,text="enter user name",font=("alice",20,"bold"),fg="black",bg="Aquamarine")
        self.userlabel.pack()

        self.userentry=Entry(self.screen,font=("alice",20,"bold"))
        self.userentry.pack()

        self.userpassword=Label(self.screen,text="enter password",font=("alice",20,"bold"),fg="black",bg="Aquamarine")
        self.userpassword.pack()

        self.passwordentry=Entry(self.screen,font=("alice",20,"bold"))
        self.passwordentry.pack()

        Label(self.screen,bg="Aquamarine").pack()


        def confirmlogin():
            myusername=self.userentry.get()
            mypassword=int(self.passwordentry.get())

            
            if myusername in username:
                verify = username.index(myusername)   
                if mypassword== password[verify]:    
                 print("login successfully!")

                else:
                    print("wrong password!")

            else:
                    print("user name not found!")


        self.confirm=Button(self.screen,text="log in",font=("alice",20,"bold"),fg="black",bg="antiquewhite",command=confirmlogin)
        self.confirm.pack()

        self.screen.mainloop()


myloginapp=loginapp()
myloginapp.login()