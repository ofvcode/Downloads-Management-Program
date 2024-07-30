from tkinter import *
from pathlib import Path
import shutil
import os
Home = str(Path.home())
downloadsDirectory = Home +"/Downloads/"
entries = Path(downloadsDirectory)
root=Tk()
root.title("File Management Program")

# MADE BY OFV


#Define Functions

def CheckFolders():
      picPathExist = os.path.exists(downloadsDirectory +"Downloaded Pictures/")
      isoPathExist = os.path.exists(downloadsDirectory +"Downloaded ISO Files/")
      debPathExist = os.path.exists(downloadsDirectory +"Downloaded Linux Files/")
      textPathExist = os.path.exists(downloadsDirectory +"Downloaded Text Files/")
      zipPathExist = os.path.exists(downloadsDirectory +"Downloaded Zip Files/")
      execPathExist = os.path.exists(downloadsDirectory +"Downloaded Executable Files/")
      if picPathExist == True: 
         print("Picture Path Exists")
      else:
         print("Picture Folder did not exist !")
         os.mkdir(downloadsDirectory + "Downloaded Pictures/")
         print("Downloads Picture Folder directory has been made !")
      if isoPathExist == True: 
         print(" ISO Path Exists")
      else:
         print("ISO Folder did not exist !")
         os.mkdir(downloadsDirectory + "Downloaded ISO Files/")
         print("Downloads ISO Folder directory has been made !")
      if debPathExist == True: 
         print(" Linux Path Exists")
      else:
         print("Linux Folder did not exist !")
         os.mkdir(downloadsDirectory + "Downloaded Linux Files/")
         print("Downloads Linux Folder directory has been made !")
      if textPathExist == True: 
         print("Text Path Exists")
      else:
         print("Text Folder did not exist !")
         os.mkdir(downloadsDirectory + "Downloaded Text Files/")
         print("Downloads Text Folder directory has been made !")
      if zipPathExist == True: 
         print("Zip Path Exists")
      else:
         print("Zip Folder did not exist !")
         os.mkdir(downloadsDirectory + "Downloaded Zip Files/")
         print("Downloads Zip Folder directory has been made !")
      if execPathExist == True: 
         print("Executable Path Exists")
      else:
         print("Executable Folder did not exist !")
         os.mkdir(downloadsDirectory + "Downloaded Executable Files/")
         print("Downloads Executable Folder directory has been made !")
    
         



def moveImages():
    CheckFolders()
    for f_name in os.listdir(entries):
     if f_name.endswith(('.jpg' , '.png' , 'gif', 'ico')):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Pictures/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Pictures/" + f_name)
    print("Complete!")
   
def moveDeb():
    CheckFolders()
    for f_name in os.listdir(entries):
     if f_name.endswith(('.deb','tar.xz', '.flatpakref')):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Linux Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Linux Files/" + f_name)
    print("Complete!")

def moveISO():
    CheckFolders()
    for f_name in os.listdir(entries):
     if f_name.endswith('.iso'):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded ISO Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded ISO Files/" + f_name)
    print("Complete!")

def moveZIP():
    CheckFolders()
    for f_name in os.listdir(entries):
     if f_name.endswith('.zip'):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Zip Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Zip Files/" + f_name)
    print("Complete!")

def moveTextFiles():
    CheckFolders()
    for f_name in os.listdir(entries):
     if f_name.endswith(('.html', '.css', '.txt' , '.pdf', '.word' , '.pptx', 'ppt' , '.doc' ,'.docx','.docm','.xml','.rtf','.dotx','.dotm','.mht','.xls','.xlsx','.csv','.xml')):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Text Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Text Files/" + f_name)
    print("Complete!")

def moveExecutableFiles():
    CheckFolders()
    for f_name in os.listdir(entries):
     if f_name.endswith(('.exe' , '.msi','.EXE')):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Executable Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Executable Files/" + f_name)
    print("Complete!")


#Define Buttons and Labels
Label1 = Label(root, text = "Please note by clicking a button it auto creates all directories!")
Label2 = Label(root, text = "* THIS PROJECT IS OPEN SOURCE & MADE BY OFVCODE ON GITHUB *")
Button1 = Button(root, text="Organize Image Download Files", padx = 40, pady= 20 ,command=moveImages)
Button2 = Button(root, text="Organize Linux Download Files", padx = 40, pady= 20 ,command=moveDeb)
Button3 = Button(root, text="Organize ISO Download Files", padx = 40, pady= 20 ,command=moveISO)
Button4 = Button(root, text="Organize Text Download Files", padx = 40, pady= 20 ,command=moveTextFiles)
Button5 = Button(root, text="Organize Zip Download Files", padx = 40, pady= 20 ,command=moveZIP)
Button6 = Button(root, text="Organize Executable Download Files", padx = 40, pady= 20 ,command=moveExecutableFiles)


#Place Buttons
Label1.grid(row=0, column=0)
Button1.grid(row=1, column=0)
Button2.grid(row=2, column=0)
Button3.grid(row=3, column=0)
Button4.grid(row=4, column=0)
Button5.grid(row=5, column=0)
Button6.grid(row=6, column=0)
Label2.grid(row=7, column=0)


#Loops the app to keep the GUI Open
root.mainloop()
