from tkinter import *  # GUI Library

# Main window
root = Tk()
root.title("EnglishToCode")

frame = Frame(root, width=300, height=300, bg="black")
frame.pack()

entry = Entry(root, text="Please enter a phrase: ")
entry.pack()

# Displays on the screen
root.mainloop()
