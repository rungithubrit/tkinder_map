from tkinter import *
import tkintermapview
from safty import open_safty
def open_home():
    root=Tk()
    root.geometry('1400x750')
    root.configure(bg="#FFFFFF")
    root.title("Main page")
    #side
    cn_side=Canvas(root,bg="#968888",height='1400',width='230',borderwidth=0).place(x=0,y=0)
    #up
    cn_up=Canvas(root,bg="#D9D9D9",height='100',width='1400',borderwidth=0).place(x=0,y=0)
    label=Label(cn_up,text="Vessel Name :",font=("Arial",30),bg="#D9D9D9").place(x=10,y=25)
    #left buttons
    b1=Button(cn_side,text="Weather",bg="#D9D9D9",font=("Arial",16),borderwidth=0,width=15,).place(x=20,y=225)
    b2=Button(cn_side,text="ETA",bg="#D9D9D9",font=("Arial",16),borderwidth=0,width=15,).place(x=20,y=300)
    b4=Button(cn_side,text="Home",bg="#D9D9D9",font=("Arial",16),borderwidth=0,width=15).place(x=20,y=150)
    b5=Button(cn_side,text="Safety check",bg="#D9D9D9",command=open_safty,font=("Arial",16),borderwidth=0,width=15).place(x=20,y=375)
    label1=LabelFrame(root)
    label1.place(x=300,y=125)
    mapwig=tkintermapview.TkinterMapView(label1,width=700,height=400,corner_radius=0)
    mapwig.pack()
    #ri8 
    cn_right=Canvas(root,bg="#968888",height='515',width='250',borderwidth=0).place(x=1050,y=125)
    dts_lb=Label(cn_right,text="Details",font=("Arial" ,18, "bold"),bg="#968888").place(x=1125,y=175)
    long_lb=Label(cn_right,text="Longitude:",font=("Arial" ,18),bg="#968888").place(x=1100,y=225)
    longt_lb=Label(cn_right,text="92.11",font=("Arial" ,18),bg="#968888").place(x=1100,y=275)
    lat_lb=Label(cn_right,text="Latitude:",font=("Arial" ,18),bg="#968888").place(x=1100,y=325)
    latt_lb=Label(cn_right,text="92.11",font=("Arial" ,18),bg="#968888").place(x=1100,y=375)
    spd_lb=Label(cn_right,text="Speed:",font=("Arial" ,18),bg="#968888").place(x=1100,y=425)
    spdt_lb=Label(cn_right,text="21km/h",font=("Arial" ,18),bg="#968888").place(x=1100,y=475)

    #home
    dep=Label(root,text=("Depature   ---> "),font=("Arial",18,"bold"),bg="#FFFFFF").place(x=475,y=600)
    arr=Label(root,text=(" Arrival "),font=("Arial",18,"bold"),bg="#FFFFFF").place(x=650,y=600)
    dep_lb=Label(cn_right,text="Cochin",font=("Arial" ,18),bg="#FFFFFF").place(x=475,y=650)
    arr_lb=Label(cn_right,text="Cochin",font=("Arial" ,18),bg="#FFFFFF").place(x=655,y=650)
    root.mainloop()

if __name__ == "__main__":
    open_home()
