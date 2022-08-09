from tkinter import*
import sqlite3

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    username text,
                    email text, 
                    contact number
                )
            ''')
con.commit()

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Fullname",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Username",width=20,font=("bold", 10))
label_2.place(x=70,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Email Id",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Number",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

entry_4 = Entry(root)
entry_4.place(x=240,y=280)

def add_details():
    con = sqlite3.connect('userdata.db')
    cur = con.cursor()
    cur.execute("INSERT INTO record VALUES (:name, :username, :email, :contact)", {
        'name': entry_1.get(),
        'username': entry_2.get(),
        'email': entry_3.get(),
        'contact': entry_4.get()

    })
    con.commit()
    import login

Button(root, text='Submit', width=20, bg='brown', fg='white', command=add_details).place(x=180, y=380)
print("registration form  successfully created...")

root.mainloop()
