from tkinter import *
#from PIL import Image,ImageTK
def open_safty():
    root=Tk()
    root.geometry("1400x750")
    root.configure(bg='#0F2167')
    root.title("safety check")
    #hom_bt=PhotoImage(file='homelogo2.png')
    btn=Button(root,text='Home',borderwidth=0,font=('Arial',14)).place(x=2,y=2)
    cn=Canvas(root,bg='#FFFFFF',height='500',width="700").place(x=70,y=20)
    cn1=Canvas(root,bg='#FFFFFF',height='400',width="500").place(x=820,y=20)
    btn1=Button(root,text='Start',bg='#FFFFFF',font=("Arial",20),borderwidth=0,width=7).place(x=220,y=600)
    btn2=Button(root,text='Stop',bg='#FFFFFF',font=("Arial",20),borderwidth=0,width=7).place(x=420,y=600)
    def thing():
        lbl=Label(root,text='Description:',font=("Arial",20),bg='#0F2167',fg='#FFFFFF').place(x=820,y=550)
        TextArea=Text(root,font=('Arial',20),height=4,width=33).place(x=820,y=600)
    btn3=Button(root,text='Generate Report',bg='#FFFFFF',font=("Arial",20),borderwidth=0,command=thing).place(x=970,y=450)


    root.mainloop()
if __name__ == "__main__":
    open_safty()
