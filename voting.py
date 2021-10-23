from tkinter import *
from tkinter import messagebox

#count=0
#global count1=0
count=0

def hello():
    global count
    
    print("HY Ritik this side !!!")
    messagebox.showinfo("Welcome Superpower2020","Welcome to the Detention Centre\n#Copied from China")
    count =count+1
    
def chutiya():
    global count1
    count1=0
    messagebox.showinfo("","Do we even exist!!!")
    count1=count1+1
def dev():
    global count2
    count2=0
    messagebox.showinfo("","Development Asap")
    count2=count2+1

def end ():
    global count
    global count1
    global count2
    print("AAp:",count2)
    print("BJP:",count)
    print("CONG:",count)
    
    
tc=Tk()
tc.geometry("500x500")
ab=Button(tc,text="AAP",bg="black",fg="white",command=dev)
cg=Button(tc,text="Cong",bg="Green",fg="white",command=chutiya)
gb=Button(tc,text="BJP",bg="orange",fg="white",command= hello )
gg=Label(tc,text="Voting day today:",font=("product sans",30,""))
ag=Button(tc,text="End Result ",bg="black",fg="white",command=end)
ag.pack()
gg.pack()
gb.place(x=5,y=70)
gb.config(height=5,width=10)
#gb.pack()
#ab.pack()
ab.place(x=100,y=70)
ab.config(height=5,width=10)

#cg.pack()
cg.place(x=200,y=70)
cg.config(height=5,width=10)

