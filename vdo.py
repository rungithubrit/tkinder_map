import tkinter as tk
from tkinter_webcam import webcam
import cv2
root=tk.Tk()
root.title("video")
root.geometry("500x500")
video=webcam.Box(root,width=500,height=500)
video.show_frames()
tk.mainloop()