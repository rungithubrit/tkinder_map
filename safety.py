
from tkinter import *
from PIL import ImageTk,Image
from tkinter_webcam import webcam
import cv2
root=Tk()
root.geometry("1400x750")
root.configure(bg='#0F2167')
root.title("safety check")
#hom_bt=PhotoImage(file='homelogo2.png')
cn=Canvas(root,bg='#FFFFFF',height='500',width="650")
video=webcam.Box(cn,width=650,height=500)
video.show_frames()
cn.place(x=140,y=20)
cn1=Canvas(root,bg='#FFFFFF',height='400',width="500").place(x=860,y=20)
btn1=Button(root,text='Start',bg='#FFFFFF',font=("Arial",20),borderwidth=0,width=7).place(x=290,y=600)
btn2=Button(root,text='Stop',bg='#FFFFFF',font=("Arial",20),borderwidth=0,width=7).place(x=490,y=600)
pic=Image.open('pillayare2.jpeg')
resized=pic.resize((100,100))
newpic=ImageTk.PhotoImage(resized)
piclab=Button(image=newpic,borderwidth=0,bg="#0F2167").place(x=20,y=20)
def thing():
    lbl=Label(root,text='Description:',font=("Arial",20),bg='#0F2167',fg='#FFFFFF').place(x=860,y=550)
    TextArea=Text(root,font=('Arial',20),height=4,width=33).place(x=860,y=600)
btn3=Button(root,text='Generate Report',bg='#FFFFFF',font=("Arial",20),borderwidth=0,command=thing).place(x=970,y=450)
root.mainloop()