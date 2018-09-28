from tkinter import *  # GUI Library
import math as m

# Main window
root = Tk()
root.title("EnglishToCode")

frame = Frame(root, width=500, height=500, bg="black")
frame.pack()

prompt_text = Label(root, text="Please enter something:")
prompt = Entry(root)
prompt_text.pack(side=LEFT)
prompt.pack(side=LEFT)


# Displays on the screen
root.mainloop()
