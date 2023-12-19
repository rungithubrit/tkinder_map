
from tkinter import *
root=Tk()
root.geometry('1400x750')
root.configure(bg="#FFFFFF")
root.title("login page")
cn=Canvas(root,bg="#0F2167",height='1400',width='446').place(x=0,y=0)
label=Label(root,text="Login page",font=("Arial",24),bg="#FFFFFF").place(x=600,y=20)
label1=Label(root,text="User Name or Email",font=("Arial",20),bg="#FFFFFF").place(x=600,y=190)
label2=Label(root,text="Password",font=("Arial",20),bg="#FFFFFF").place(x=600,y=400)
entry1=Entry(root,font=("Arial",24),bg="#D9D9D9")
entry1.place(x=600,y=270)
entry2=Entry(root,font=("Arial",24),bg="#D9D9D9")
entry2.place(x=600,y=480)
label=Label(root,text="New user?",font=("Arial",24),bg="#FFFFFF").place(x=600,y=600)
b1=Button(root,text="Register here", command=open_dialog, bg="#0F2167",fg="#FFFFFF",font=("Arial",20),borderwidth=0).place(x=800,y=600)

root.mainloop()



