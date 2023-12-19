import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):

	def _init_(self, *args, **kwargs): 
		
		tk.Tk._init_(self, *args, **kwargs)
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.frames = {} 

		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):
	def _init_(self, parent, controller): 
		tk.Frame._init_(self, parent)
        #root=Tk()
        #root.geometry('1400x750')
        #root.configure(bg="#FFFFFF")
        #root.title("login page")
        cn=Canvas(self,bg="#0F2167",height='1400',width='446').place(x=0,y=0)
        label=Label(self,text="Login page",font=("Arial",24),bg="#FFFFFF").place(x=600,y=20)
        label1=Label(self,text="User Name or Email",font=("Arial",20),bg="#FFFFFF").place(x=600,y=190)
        label2=Label(self,text="Password",font=("Arial",20),bg="#FFFFFF").place(x=600,y=400)
        entry1=Entry(self,font=("Arial",24),bg="#D9D9D9")
        entry1.place(x=600,y=270)
        entry2=Entry(self,font=("Arial",24),bg="#D9D9D9")
        entry2.place(x=600,y=480)
        label=Label(self,text="New user?",font=("Arial",24),bg="#FFFFFF").place(x=600,y=600)
        b1=Button(root,text="Register here",bg="#0F2167",fg="#FFFFFF",font=("Arial",20),borderwidth=0).place(x=800,y=600)
        root.mainloop()

class Page1(tk.Frame):
	
	def _init_(self, parent, controller):
		
		tk.Frame._init_(self, parent)
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))

		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="Page 2",
							command = lambda : controller.show_frame(Page2))

		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

class Page2(tk.Frame): 
	def _init_(self, parent, controller):
		tk.Frame._init_(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="Page 1",
							command = lambda : controller.show_frame(Page1))

		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))

		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

app = tkinterApp()
app.mainloop()