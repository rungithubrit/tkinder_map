import tkinter as tk
from tkinter import ttk

class PannedWindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panned Window with Navigation")

        # Create a PanedWindow
        self.paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)

        # Create frames to be added to the paned window
        self.frame1 = ttk.Frame(self.paned_window, width=200, height=400, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.paned_window, width=200, height=400, relief=tk.SUNKEN)
        self.frame3 = ttk.Frame(self.paned_window, width=200, height=400, relief=tk.SUNKEN)

        # Add frames to the paned window
        self.paned_window.add(self.frame1)
        self.paned_window.add(self.frame2)
        self.paned_window.add(self.frame3)

        # Create navigation buttons
        self.prev_button = ttk.Button(root, text="Previous", command=self.show_previous)
        self.next_button = ttk.Button(root, text="Next", command=self.show_next)
        self.next_button2 = ttk.Button(root, text="Next2", command=self.show_next2)

        # Pack the paned window and buttons
        self.paned_window.pack(expand=True, fill=tk.BOTH)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        self.next_button.pack(side=tk.RIGHT, padx=5)
        self.next_button2.pack(side=tk.BOTTOM, padx=5)  

        # Initialize the current frame index
        self.current_frame_index = 0

        # Create some content in the frames (you can customize this part)
        label1 = ttk.Label(self.frame1, text="Frame 1 Content")
        label1.pack(pady=20)

        label2 = ttk.Label(self.frame2, text="Frame 2 Content")
        label2.pack(pady=20)

        label3 = ttk.Label(self.frame3, text="Frame 3 Content")
        label3.pack(pady=20)

    def show_previous(self):
        if self.current_frame_index > 0:
            self.current_frame_index -= 1
            self.paned_window.sash_place(self.current_frame_index, 0)
           
    def show_next(self):
        if self.current_frame_index < 1:
            self.current_frame_index += 1
            self.paned_window.sash_place(self.current_frame_index, self.paned_window.winfo_width() - 4)

    def show_next2(self):
        if self.current_frame_index < 2:
            self.current_frame_index += 2
            self.paned_window.sash_place(self.current_frame_index, self.paned_window.winfo_width() - 4)


if __name__ == "__main__":
    root = tk.Tk()
    app = PannedWindowApp(root)
    root.mainloop()
