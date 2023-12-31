from tkinter import *
from PIL import ImageTk,Image
import tkintermapview
root=Tk()
root.geometry("1400x750")
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
root.mainloop()