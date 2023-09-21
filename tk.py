from tkinter import *
from PIL import ImageTk, Image

window = Tk(className='התנדבות בהתאמה אישית')
window.geometry("1100x650")


frame = Frame(window, width=1100, height=600)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
image = ImageTk.PhotoImage(Image.open("Backround.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image=image)
label.pack()

window.mainloop()
