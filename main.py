import folium
from tkinter import Frame, Tk, PhotoImage, Label
import webbrowser
root = Tk()
root.geometry("800x600")

# Create a Tkinter frame
frame = Frame(root)
frame.place(relwidth=1, relheight=1)

# Create a Folium map
m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

# Save the map as an HTML file
m.save("map.html")
webbrowser.open("map.html")
