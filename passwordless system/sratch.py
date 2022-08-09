from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkinter import Tk, Label, Button, filedialog, messagebox


class DriveUpload:
    def __init__(self, master):
        self.master = master
        self.sourcePath = ''
        self.filename = ''
        self.drive = GoogleDrive()

        master.title('Upload File to Google Drive')

        button1 = Button(self.master, text="Authenticate Credentials", command=self.Auth)
        button1.grid(row=0, column=0)
        self.label1 = Label(self.master, text="Not Authenticated!")
        self.label1.grid(row=0, column=1)

        label2 = Label(self.master, text="Choose File to Upload")
        label2.grid(row=1)
        button2 = Button(self.master, text="Browse", command=self.ChooseFile)
        button2.grid(row=1, column=1, columnspan=3)

        label3 = Label(self.master, text="File Chosen")
        label3.grid(row=2)

        self.label4 = Label(self.master)
        self.label4.grid(row=2, column=1, columnspan=3)
        self.label4['text'] = ''

        button3 = Button(self.master, text="Upload", command=self.UploadFile)
        button3.grid(row=3, columnspan=3)

    def Auth(self):
        try:
            g_login = GoogleAuth()
            g_login.LocalWebserverAuth()
            self.drive = GoogleDrive(g_login)
            messagebox.showinfo("Confirmation", "Authentication Succeeded! Upload File!")
            self.label1['text'] = "Authenticated!"
        except:

            return

    def ChooseFile(self):
        self.sourcePath = filedialog.askopenfilename()
        self.filename = self.sourcePath[self.sourcePath.rfind('/') + 1:]
        self.label4['text'] = self.filename

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


def main():
    root = Tk()
    root.geometry("250x100")
    DriveUpload(root)
    root.mainloop()


if __name__ == "__main__":
    main()
