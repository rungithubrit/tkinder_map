import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image
from tkinter_webcam import webcam
import cv2
class PannedWindowApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Panned Window with Navigation")

        # Create a PanedWindow
        self.paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)

        # Create navigation buttons
        self.frame1 = ttk.Frame(self.paned_window, width=900, height=800, relief=tk.SUNKEN)
        # Add the new frame to the paned window
        self.paned_window.add(self.frame1)
        self.label1 = ttk.Label(root,width=300,height=400 )
        self.label2 = ttk.Label(root, text="Next", command=self.show_next)
        self.label1.pack(side=tk.LEFT, padx=5)
        self.label2.pack(side=tk.RIGHT, padx=5)

        # Create a list to store frame references
        self.frames = []
if __name__ == "__main__":
    root = tk.Tk()
    app = PannedWindowApp(root)
    root.mainloop()    