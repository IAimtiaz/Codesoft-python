import  tkinter
from tkinter import *

root=Tk()
root.title("To do list ")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list=[]
def addtask():
    task= task_entry.get()
    task_entry.delete(0,END)

    if task :
        with open ("tasklist.txt",'a')as taskfile:
            taskfile.write(f"/n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open ("tasklist.txt",'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
                
            listbox.delete(ANCHOR)       

def openTaskFile():


    try:
        
        global task_list
        with open("tasklist.txt","r") as taskfile:
              tasks= taskfile.readlines()

        for task in task :
              if task !='/n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt','w')
        file.close()
              




#icon


Image_icon=PhotoImage(file="pic/task.png")
root.iconphoto(False,Image_icon)


#TOP BAR

TopImage=PhotoImage(file="pic/topbar.png")
Label(root,image=TopImage).pack()

docImage=PhotoImage(file="pic/dock.png")
Label (root,image=docImage,bg="#32405b").place(x=30,y=25)

noteImage=PhotoImage(file="pic/task.png")
Label(root,image=noteImage,bg="#32405b").place(x=340,y=25)

heading=Label(root,text="REMEMBER",font="chiller 20 bold ", fg="black" ,bg="#778899")
heading.place(x=130,y=20)

#MAIN

frame= Frame(root,width=400,height=50,bg="black")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="SAVE", font=" arial 20 bold", width=6,bg="#FF6347", fg="#fff", bd=0,command=addtask)
button.place(x=300,y=0)

#LIST BOX CREATION

frame1=Frame(root,bd=3,width=700,height=280,bg="")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=('arial',12),width=40,height=16,bg="#DAA520",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill= BOTH, padx=2)


scrollbar=Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill= BOTH)
mylist = Listbox(root, 
                 yscrollcommand = scrollbar.set )

listbox.config(yscrollcommand= scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
              
#DELETING BUTTON 

Delete_icon=PhotoImage(file="pic/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
button.place(x=300,y=0)




root.mainloop()
                      
                      
