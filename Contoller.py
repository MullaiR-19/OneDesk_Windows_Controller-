from tkinter import *
import os
import time
win = Tk()
win.title("%Controller%")
win.geometry("220x150")


def devic_mgr():
    os.system("devmgmt.msc")

def systemConfig():
    os.system("msconfig")

def shutdown():
    os.system("Shutdown /s /f /t 00")

def restart():
    os.system("shutdown /r /f /t 00")

def controlPanel():
    os.system("control panel")

def temp():
	
    os.system("Del /s /f /q%temp%")
    time.sleep(2)
    os.system("Del /s /f /q%Windir%\Temp")
    time.sleep(2)


button1=Button(win, text= "Shutdown PC", command = shutdown, height =3,width =17)
button1.grid(row =0,column=0)

button2=Button(win, text= "Restart PC", command = restart, height =3,width =17)
button2.grid(row=0,column=1)

button3=Button(win, text= "System Config", command = systemConfig, height =3,width =17)
button3.grid(row =1,column=0)

button4=Button(win, text= "Device Manager", command = devic_mgr, height =3,width =17)
button4.grid(row=1,column=1)

button5=Button(win, text= "Control Panel", command = controlPanel, height =3,width =17)
button5.grid(row =2,column=0)

button6=Button(win, text= "Temp Clear", command = temp, height =3,width =17)
button6.grid(row=2,column=1)
        
win.mainloop()
