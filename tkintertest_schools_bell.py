import time
from tkinter import *
from tkinter import messagebox
from subprocess import call
 
# initialise main window
def __init__(win):
	win.title("School Bell ringing")
	win.attributes('-fullscreen',True)
	
 
# button callback
def on():
	messagebox.showinfo("ON", "Turning relay ON")
	command = "sudo  /usr/bin/hidusb-relay-cmd on ALL".split()
	call(command)

def off():
	messagebox.showinfo("OFF","Turning relay OFF")
	command = "sudo  /usr/bin/hidusb-relay-cmd off ALL".split()
	call(command)
def timerCountDown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label=Label(win,text=timer, font="Helvetica 16").grid(row=4,column=4, padx=10,pady=10)
        print(timer, end="\r")
        win.after(1000,timerCountDown,t-1)
        
       
def close():
	win.quit()
 
# create top-level window
win = Tk()
 
# Gets the requested values of the height and widht.
windowWidth = win.winfo_reqwidth()
windowHeight = win.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(win.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(win.winfo_screenheight()/2)
 
# Positions the window in the center of the page.
win.geometry("+{}+{}".format(positionRight, positionDown))

 #create the Smena label
lblSmenaTitl=Label(win,text="Smena", font="Helvetica 26").grid(row=0,column=0,padx=15,pady=55)

varSmena="PREPODNEVNA"
varCasovi="NORMALNI"
varTrajanjeCasa="45"
varUTokuJe="Veliki odmor"
varTrajeDo="9:35"
varTrajanjeOdmora="1"

lblSmenaValue=Label(win,text=varSmena,font="Helvetica 30 bold").grid(row=0,column=1,padx=15,pady=55)

#Casovi labels
lblCasoviTitle=Label(win,text="Casovi", font="Helvetica 16").grid(row=1, column=0,padx=15,pady=55)
lblCasoviValue=Label(win,text=varCasovi,font="Helvetica 30 bold").grid(row=1,column=1,padx= 5,pady=55)
lblCasoviTrajanjeTitl=Label(win,text="Trajanje",font="Helvetica 16").grid(row=1,column=2,padx=5,pady=55)
lblCasoviTrajanjeValue=Label(win,text=varTrajanjeCasa + " minuta",font="Helvetica 30 bold").grid(row=1,column=3,padx=5,pady=55)
lblUTokuJeTitle=Label(win,text="U toku je:", font="Helvetica 16").grid(row=2,column=2,padx=5,pady=55)
lblUTokuJeValue=Label(win,text=varUTokuJe,font="Helvetica 36 bold").grid(row=3, column=2, padx=5, pady=55)
lblTrajeDoTitle=Label(win,text="traje do:", font="Helvetica 16").grid(row=4,column=1, padx=10, pady=15, sticky=E)
lblTrajeDoValue=Label(win,text=varTrajeDo + ", ", font="Helvetica 30 bold").grid(row=4, column=2, padx=10, pady=55, sticky=W)
lblOstaloJos=Label(win,text="do zvona ostalo jos: ",font="Helvetica 16").grid(row=4,column=3)

# create a button
btnSettins=Button(win,text="Podesavanja", width=60, height=3, font="Helvetica 14") .grid(row=5,column=2, padx=55, pady=250)
btnClose=Button(win,text="Zatvori" ,width=40,height=3, font="Helvetica 14",command=close).grid(row=5,column=3,padx=35,pady=150)
#for i in range(int(varTrajanjeOdmora)*60,0,-1):
#	timerCountDown(i)
# initialise and start main loop

#ovde sam nesato promenio
__init__(win)
mainloop()
