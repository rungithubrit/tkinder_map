from tkinter import *
from main import open_home
def open_dialog():
    
    root=Tk()
    root.geometry("1400x750")
    root.configure(bg="#0F2167")
    root.title("Register page")
    label1=Label(root,text="Register page",font=("Arial",28),bg="#0F2167",fg="#FFFFFF").place(x=600,y=50)
    label2=Label(root,text="Name",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=80,y=150)
    label3=Label(root,text="Email Id",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=80,y=350)
    label4=Label(root,text="Password",font=("Arial",24),bg="#0F2167",fg="#FFFFFF").place(x=80,y=550)
    entry1=Entry(root,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=240,y=150)
    entry2=Entry(root,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=240,y=350)
    entry3=Entry(root,font=('Arial',24),bg="#FFFFFF",borderwidth=3).place(x=240,y=550)
    label5=Label(root,text="product key will be sent\nthrough mail in two  to \n  three business day !",font=('Italic',26),bg='#D9D9D9',padx=30,pady=30).place(x=800,y=360)
    b1=Button(root,text="Register",command=open_home,bg="#D9D9D9",font=("Arial",24),borderwidth=5).place(x=600,y=650)
    root.mainloop()

if __name__ == "__main__":
    open_dialog()
