
import tkinter as tk
from tkinter import ttk

class PannedWindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Panned Window with Navigation")

        # Create a PanedWindow
        self.paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)

        # Create navigation buttons
        self.add_frame_button = ttk.Button(root, text="Add Frame", command=self.add_frame)
        self.remove_frame_button = ttk.Button(root, text="Remove Frame", command=self.remove_frame)

        # Pack the paned window and butt
        self.paned_window.pack(expand=True, fill=tk.BOTH)
        self.add_frame_button.pack(side=tk.LEFT, padx=5)
        self.remove_frame_button.pack(side=tk.RIGHT, padx=5)

        # Create a list to store frame references
        self.frames = []

    def add_frame(self):
        # Create a new frame
        new_frame = ttk.Frame(self.paned_window, width=200, height=400, relief=tk.SUNKEN)
       
        # Add the new frame to the paned window
        self.paned_window.add(new_frame)
       
        # Add the new frame to the list
        self.frames.append(new_frame)

    def remove_frame(self):
        # Assuming you want to remove the last frame, change index as needed
        if self.frames:
            index_to_remove = len(self.frames) - 1

            # Remove the specified frame from the paned window
            self.paned_window.forget(index_to_remove)

            # Remove the specified frame from the list
            self.frames.pop(index_to_remove)

if __name__ == "__main__":
    root = tk.Tk()
    app = PannedWindowApp(root)
    root.mainloop()