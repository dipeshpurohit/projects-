from tkinter import *
import sqlite3
from tkinter import messagebox


root = Tk()
root.geometry('500x500')
root.title("Login")

label_0 = Label(root, text="Login",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Username",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email ID",width=20,font=("bold", 10))
label_2.place(x=70,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

def login_response():

    try:
        db = sqlite3.connect('userdata.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM record where username=? AND email=?", (entry_1.get(), entry_2.get()))
        row = cursor.fetchone()
        if row:
            username = row[1]
            email = row[2]
            messagebox.showinfo('infor', 'login successful')
            import Token
        else:
            messagebox.showinfo('info', 'login failed')
        cursor.connection.commit()
        db.close()

    except:
        messagebox.showerror("login failed")


def register():
    import regestration


Button(root, text='login',width=20,bg='brown',fg='white', command=login_response).place(x=180,y=250)
Button(root, text='register',width=20,bg='brown',fg='white', command=register).place(x=180,y=350)


root.mainloop()
print("login successfully")