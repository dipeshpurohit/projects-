from tkinter import *
from tkinter import messagebox
import smtplib
import random

root = Tk()
root.title("Send OTP Via Email")
root.geometry("1040x540")

email_label = Label(root, text="Enter receiver's Email: ", font=("ariel 15 bold"), relief=FLAT)
email_label.grid(row=0, column=0, padx=15, pady=60)
email_entry = Entry(root, font=("ariel 15 bold"), width=25, relief=GROOVE, bd=2)
email_entry.grid(row=0, column=1, padx=12, pady=60)
email_entry.focus()

code_label = Label(root, text="Enter Code: ", font=("ariel 15 bold"), relief=FLAT)
code_label.grid(row=2, column=3, padx=15, pady=60)
code_entry = Entry(root, font=("ariel 15 bold"), width=25, relief=GROOVE, bd=2)
code_entry.grid(row=2, column=4, padx=12, pady=60)


sender = "darkwarrio2511@gmail.com"
password = "Dark2511"

OTP=""
for i in range(4):
    OTP = random.randint(1000, 9999)
    OTP = str(OTP)
otp = OTP

def send():
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender, email_entry.get(), otp)
        messagebox.showinfo("Code sent", f"Code sent to {email_entry.get()}")
        s.quit()


    except:
        messagebox.showinfo("Send OTP via Email",
                            "Please enter the valid email address OR check an internet connection")

def submit():
    if code_entry.get() == OTP:
        messagebox.showinfo("login succesfully")
        import portal
    else:
        messagebox.showinfo("login failed")




send_button = Button(root, text="Send Email", font=("ariel 15 bold"), bd=3, command=send)
send_button.place(x=210, y=150)

send_button = Button(root, text="Submit code", font=("ariel 15 bold"), bd=3, command=submit)
send_button.place(x=800, y=300)

root.mainloop()





