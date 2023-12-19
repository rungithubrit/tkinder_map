#login

from tkinter import *
from PIL import ImageTk,Image
from tkinter_webcam import webcam
import cv2
import tkintermapview
root=Tk()
root.geometry('1400x750')
def login():
    root.configure(bg="#FFFFFF")
    root.title("login page")
    cn=Canvas(root,bg="#0F2167",height='1400',width='446').place(x=0,y=0)
    #logo
    pic=Image.open('pillayare2.jpeg')
    resized=pic.resize((300,300))
    newpic=ImageTk.PhotoImage(resized)
    piclab=Label(cn,image=newpic,borderwidth=0,bg="#0F2167").place(x=60,y=200)
    #logo2
    pic2=Image.open('sihlogo.png')
    resizedpic2=pic2.resize((100,100))
    newpic2=ImageTk.PhotoImage(resizedpic2)
    pic2lab=Label(root,image=newpic2,borderwidth=0,bg="#FFFFFF").place(x=750,y=70)
    label=Label(cn,text="Vessel360",font=("Arial",46,"bold"),bg="#0F2167",fg="#FFFFFF").place(x=60,y=82)
    labellog=Label(cn,text="Login",font=("Arial",20,"bold"),bg="#0F2167",fg="#FFFFFF").place(x=155,y=512)
    label1=Label(root,text="Roll ID",font=("Arial",20),bg="#FFFFFF").place(x=600,y=190)
    label2=Label(root,text="Password",font=("Arial",20),bg="#FFFFFF").place(x=600,y=370)
    entry1=Entry(root,font=("Arial",24),bg="#D9D9D9")
    entry1.place(x=600,y=270)
    entry2=Entry(root,font=("Arial",24),bg="#D9D9D9")
    entry2.place(x=600,y=450)
    label=Label(root,text="New user?",font=("Arial",24),bg="#FFFFFF").place(x=600,y=600)
    b1=Button(root,text="Click here...",bg="#FFFFFF",fg="#0F2167",font=("Arial",20),borderwidth=0,command=regi).place(x=780,y=595)
    b2=Button(root,text="Login",bg="#0F2167",fg="white",font=("Arial",20),borderwidth=0,width=7,command=map).place(x=710,y=510)


#register

def regi():
    root.configure(bg="#0F2167")
    root.title("Register page")
    label1=Label(root,text="Create Your Account",font=("Arial",28),bg="#0F2167",fg="#FFFFFF").place(x=600,y=50)
    label2=Label(root,text="Name",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=400,y=200)
    label3=Label(root,text="Email Id",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=400,y=340)
    label4=Label(root,text="Password",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=400,y=500)
    entry1=Entry(root,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=600,y=200)
    entry2=Entry(root,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=600,y=340)
    entry3=Entry(root,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=600,y=500)
    pic=Image.open('pillayare2.jpeg')
    resized=pic.resize((150,150))
    newpic=ImageTk.PhotoImage(resized)
    piclab=Label(root,image=newpic,borderwidth=0,bg="#0F2167").place(x=20,y=20)
    b1=Button(root,text="Register",bg="#D9D9D9",font=("Arial",24),borderwidth=5,width=15,command=login).place(x=640,y=650)

if __name__ == "__main__":
    regi()

#map


def map():
    root.configure(bg="#FFFFFF")
    root.title("Main page")
    #side
    cn_side=Canvas(root,bg="#818FB4",height='1400',width='230',borderwidth=0).place(x=0,y=0)
    #up
    cn_up=Canvas(root,bg="#A9B8E1",height='100',width='1400',borderwidth=0).place(x=0,y=0)
    label=Label(cn_up,text="Vessel Name :",font=("Arial",30),bg="#A9B8E1").place(x=300,y=25)
    #logo
    pic=Image.open('pillayare2.jpeg')
    resized=pic.resize((80,80))
    newpic=ImageTk.PhotoImage(resized)
    piclab=Label(cn_up,image=newpic,borderwidth=0,bg="#A9B8E1").place(x=15,y=15)
    #left buttons
    b1=Button(cn_side,text="Weather",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white').place(x=20,y=225)
    b2=Button(cn_side,text="ETA",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white',command=lambda:eta()).place(x=20,y=300)
    b4=Button(cn_side,text="Home",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white').place(x=20,y=150)
    b5=Button(cn_side,text="Safety check",bg="#363062",font=("Arial",16),borderwidth=0,width=15,fg='white',command=lambda:safe()).place(x=20,y=375)
    label1=LabelFrame(root)
    label1.place(x=300,y=125)
    mapwig=tkintermapview.TkinterMapView(label1,width=700,height=400,corner_radius=0)
    mapwig.pack()
    #ri8 
    cn_right=Canvas(root,bg="#818FB4",height='515',width='250',borderwidth=0).place(x=1050,y=125)
    dts_lb=Label(cn_right,text="Details",font=("Arial" ,18, "bold"),bg="#818FB4").place(x=1125,y=175)
    long_lb=Label(cn_right,text="Longitude:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=225)
    longt_lb=Label(cn_right,text="92.11",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=275)
    lat_lb=Label(cn_right,text="Latitude:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=325)
    latt_lb=Label(cn_right,text="92.11",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=375)
    spd_lb=Label(cn_right,text="Speed:",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=425)
    spdt_lb=Label(cn_right,text="21km/h",font=("Arial" ,18),bg="#818FB4").place(x=1100,y=475)

    #home
    dep=Label(root,text=("Depature   ---> "),font=("Arial",18,"bold"),bg="#FFFFFF").place(x=475,y=600)
    arr=Label(root,text=(" Arrival "),font=("Arial",18,"bold"),bg="#FFFFFF").place(x=650,y=600)
    dep_lb=Label(cn_right,text="Cochin",font=("Arial" ,18),bg="#FFFFFF").place(x=475,y=650)
    arr_lb=Label(cn_right,text="Cochin",font=("Arial" ,18),bg="#FFFFFF").place(x=655,y=650)

if __name__ == "__main__":
    map()

#safety

def safe():
    
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
    piclab=Button(image=newpic,borderwidth=0,bg="#0F2167",command=map).place(x=20,y=20)
    def thing():
        lbl=Label(root,text='Description:',font=("Arial",20),bg='#0F2167',fg='#FFFFFF').place(x=860,y=550)
        TextArea=Text(root,font=('Arial',20),height=4,width=33).place(x=860,y=600)
        btn3=Button(root,text='Generate Report',bg='#FFFFFF',font=("Arial",20),borderwidth=0,command=thing).place(x=970,y=450)

if __name__ == "__main__":
    safe()

#eta

def eta():
    root.configure(bg="#0F2167")
    root.title("Departure & Arrival")
    cn=Canvas(root,bg='#FFFFFF',height='450',width='700').place(x=70,y=150)
    label1=Label(root,text="Departure port",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=150)
    label2=Label(root,text="Arrival port",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=260)
    entry1=Entry(root,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=150)
    entry2=Entry(root,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=260)
    btn1=Button(root,text='Submit',bg='#FFFFFF',font=("Arial",20),borderwidth=0,width=10).place(x=1000,y=370)
    label2=Label(root,text="ETA",font=("Arial",20),bg="#0F2167",fg="#FFFFFF").place(x=800,y=500)
    entry1=Entry(root,font=('Arial',20),bg="#FFFFFF",borderwidth=3).place(x=1000,y=500)
    pic=Image.open('pillayare2.jpeg')
    resized=pic.resize((100,100))
    newpic=ImageTk.PhotoImage(resized)
    piclab=Label(image=newpic,borderwidth=0,bg="#0F2167").place(x=20,y=20)
    #map
    label1=LabelFrame(root)
    label1.place(x=70,y=150)
    mapwig=tkintermapview.TkinterMapView(label1,width=700,height=450,corner_radius=0)
    mapwig.pack()

if __name__ == "__main__":
    eta()


login()
root.mainloop()