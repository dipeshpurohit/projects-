from tkinter import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkinter import Tk, Label, Button, filedialog, messagebox
from cryptography.fernet import Fernet

root = Tk()
root.geometry("500x500")

class DriveUpload:
    def __init__(self, master):
        self.master = master
        self.sourcePath = ''
        self.filename = ''
        self.drive = GoogleDrive()

        master.title('Upload File')

        button1 = Button(self.master, text="Authenticate Credentials", command=self.Auth)
        button1.place(x = 80, y = 100)
        self.label1 = Label(self.master, text="Not Authenticated!")
        self.label1.place(x = 300, y = 100)

        label2 = Label(self.master, text="Choose File to Upload")
        label2.place(x = 300, y = 200)
        button2 = Button(self.master, text="Browse", command=self.ChooseFile)
        button2.place(x = 80 , y = 200)

        self.label3 = Label(self.master)
        self.label3.place(x = 300, y = 300)
        self.label3['text'] = ''

        button3 = Button(self.master, text="Upload", command=self.UploadFile)
        button3.place(x = 200, y = 300)

        button4 = Button(self.master, text="download", command=self.downloadFile)
        button4.place(x=200, y=400)

    def Auth(self):
        try:
            login = GoogleAuth()
            login.LocalWebserverAuth()
            self.drive = GoogleDrive(login)
            messagebox.showinfo("Confirmation", "Authentication Successful!")
            self.label1['text'] = "Authenticated!"
        except:
            messagebox.showerror("Error", "Authentication Error!")
            return

    def ChooseFile(self):
        self.sourcePath = filedialog.askopenfilename()
        self.filename = self.sourcePath[self.sourcePath.rfind('/') + 1:]
        self.label3['text'] = self.filename
        if self.filename:
            if self:
                key = Fernet.generate_key()

            else:
                messagebox.showinfo('error','key is not saved')
            with open('mykey.key', 'wb') as mykey:
                mykey.write(key)
            with open('mykey.key', 'rb') as mykey:
                key = mykey.read()
            f = Fernet(key)
        with open(self.filename, 'rb') as original_file:
            original = original_file.read()
        encrypted = f.encrypt(original)
        with open(self.filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def UploadFile(self):
        if self.label1['text'] == 'Not Authenticated!':
            messagebox.showerror("Error", "Please Authenticate Credentials First!")
            return
        try:
            file_drive = self.drive.CreateFile({'title': self.filename})
            file_drive.SetContentFile(self.sourcePath)

            file_drive.Upload()
            messagebox.showinfo("Confirmation", "File Uploaded!")
        except:
            messagebox.showerror("Error", "File Upload Error!")

    def downloadFile(self):
        try:


            messagebox.showinfo('success', 'download complete')

        except:
            messagebox.showinfo('error', 'download failed')


DriveUpload(root)
root.mainloop()


if __name__ == "__main__":
    main()
