from tkinter import *
from tkinter import ttk
from pathlib import Path
import ttkbootstrap as ttk
import shutil
import os
Home = str(Path.home())
downloadsDirectory = Home +"/Downloads/"
entries = Path(downloadsDirectory)
root=ttk.Window(themename = 'darkly')
root.title("File Management Program")

# MADE BY OFV


#Define Functions

global functionUsed

def CheckFolders(functionUsed):
   
      picPathExist = os.path.exists(downloadsDirectory +"Downloaded Pictures/")
      isoPathExist = os.path.exists(downloadsDirectory +"Downloaded ISO Files/")
      debPathExist = os.path.exists(downloadsDirectory +"Downloaded Linux Files/")
      textPathExist = os.path.exists(downloadsDirectory +"Downloaded Text Files/")
      zipPathExist = os.path.exists(downloadsDirectory +"Downloaded Zip Files/")
      execPathExist = os.path.exists(downloadsDirectory +"Downloaded Executable Files/")

      if functionUsed == "picPath":
          if picPathExist == True: 
           print("Picture Path Exists")
          else:
           print("Picture Folder did not exist !")
           os.mkdir(downloadsDirectory + "Downloaded Pictures/")
           print("Downloads Picture Folder directory has been made !")


      if functionUsed == "isoPath":
         if isoPathExist == True: 
          print(" ISO Path Exists")
         else:
          print("ISO Folder did not exist !")
          os.mkdir(downloadsDirectory + "Downloaded ISO Files/")
          print("Downloads ISO Folder directory has been made !")

      if functionUsed == "debPath":
       if debPathExist == True: 
          print(" Linux Path Exists")
       else:
          print("Linux Folder did not exist !")
          os.mkdir(downloadsDirectory + "Downloaded Linux Files/")
          print("Downloads Linux Folder directory has been made !")
      
      
      
      if functionUsed == "textPath":
       if textPathExist == True: 
          print("Text Path Exists")
       else:
          print("Text Folder did not exist !")
          os.mkdir(downloadsDirectory + "Downloaded Text Files/")
          print("Downloads Text Folder directory has been made !")
      
      if functionUsed == "zipPath":
       if zipPathExist == True: 
          print("Zip Path Exists")
       else:
          print("Zip Folder did not exist !")
          os.mkdir(downloadsDirectory + "Downloaded Zip Files/")
          print("Downloads Zip Folder directory has been made !")
      
      if functionUsed == "execPath":
       if execPathExist == True: 
          print("Executable Path Exists")
       else:
          print("Executable Folder did not exist !")
          os.mkdir(downloadsDirectory + "Downloaded Executable Files/")
          print("Downloads Executable Folder directory has been made !")
    


def moveImages():
    global functionRan
    functionRan = "moveImages"
    CheckFolders("picPath")
    for f_name in os.listdir(entries):
     if f_name.endswith(('.jpg' , '.png' , 'gif', 'ico')):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Pictures/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Pictures/" + f_name)
    print("Complete!")
   
def moveDeb():
    CheckFolders("debPath")
    for f_name in os.listdir(entries):
     if f_name.endswith(('.deb','tar.xz', '.flatpakref')):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Linux Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Linux Files/" + f_name)
    print("Complete!")

def moveISO():
    CheckFolders("isoPath")
    for f_name in os.listdir(entries):
     if f_name.endswith('.iso'):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded ISO Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded ISO Files/" + f_name)
    print("Complete!")

def moveZIP():
    CheckFolders("zipPath")
    for f_name in os.listdir(entries):
     if f_name.endswith('.zip'):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Zip Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Zip Files/" + f_name)
    print("Complete!")

def moveTextFiles():
    CheckFolders("textPath")
    for f_name in os.listdir(entries):
     if f_name.endswith(('.html', '.css', '.txt' , '.pdf', '.word' , '.pptx', 'ppt' , '.doc' ,'.docx','.docm','.xml','.rtf','.dotx','.dotm','.mht','.xls','.xlsx','.csv','.xml')):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Text Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Text Files/" + f_name)
    print("Complete!")

def moveExecutableFiles():
    CheckFolders("execPath")
    for f_name in os.listdir(entries):
     if f_name.endswith(('.exe' , '.msi')):
         print(f_name + " has been moved to" + downloadsDirectory+ "Downloaded Executable Files/" + f_name)
         shutil.move(downloadsDirectory + f_name , downloadsDirectory + "Downloaded Executable Files/" + f_name)
    print("Complete!")


#Define Buttons and Labels
Label1 = ttk.Label(root, text = "Click an option to create a directory and auto organize files", font = "bold 11")
Label2 = ttk.Label(root, text = "* THIS PROJECT IS OPEN SOURCE & MADE BY OFVCODE ON GITHUB *")
Button1 = ttk.Button(root, text="Organize Image Download Files",command=moveImages)
Button2 = ttk.Button(root, text="Organize Linux Download Files",command=moveDeb)
Button3 = ttk.Button(root, text="Organize ISO Download Files" ,command=moveISO)
Button4 = ttk.Button(root, text="Organize Text Download Files" ,command=moveTextFiles)
Button5 = ttk.Button(root, text="Organize Zip Download Files", command=moveZIP)
Button6 = ttk.Button(root, text="Organize Executable Download Files" ,command=moveExecutableFiles)


#Place Buttons
Label1.grid(row=0, column=0,columnspan=3)
Button1.grid(row=1, column=0,columnspan=3,padx= 20 , pady= 10)
Button2.grid(row=2, column=0,columnspan=3,padx= 20 , pady= 10)
Button3.grid(row=3, column=0,columnspan=3,padx= 20 , pady= 10)
Button4.grid(row=4, column=0,columnspan=3,padx= 20 , pady= 10)
Button5.grid(row=5, column=0,columnspan=3,padx= 20 , pady= 10)
Button6.grid(row=6, column=0,columnspan=3,padx= 20 , pady= 10)
Label2.grid(row=7, column=0,columnspan=3,padx= 20 , pady= 10)


#Loops the app to keep the GUI Open
root.mainloop()
