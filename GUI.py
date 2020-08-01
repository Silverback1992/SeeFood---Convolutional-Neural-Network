# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:23:45 2020

@author: alin2
"""

from tkinter import *
from General_Functions import *
from CNN import *

# Create window object
app = Tk()

app.title("Hot-Dog Or Not Hot-Dog")
app.geometry("700x350")

app.resizable(False, False)

# Frame for filebrowser
browser_frame = Frame(app)
browser_frame.grid(row = 1, column = 1)

# Frame for other buttons
buttons_frame = Frame(app)
buttons_frame.grid(row = 2, column = 1)

# Label for picture
label_for_sample_picture = Label(app)
label_for_sample_picture.place(x = 400, y = 1)

# Filebrowser result 
filebrowser_text = Text(browser_frame, height = 2, width = 50, font=("Helvetica", 10), state = "disabled")
filebrowser_text.grid(row = 1, column = 2)

# Text widget for prediction
prediction_text = Text(app, height = 1, width = 25, font=("Helvetica", 10), state = "disabled")
prediction_text.place(x = 440, y = 300)

# Filebrowser button
# Image for button
browser_image = PhotoImage(file = "file-browser-icon-4.jpg", master = app)
browser_image = browser_image.subsample(30, 30)

# Putting the button down
browse_btn = Button(browser_frame, image = browser_image, height = 30, width = 30, command = lambda : get_sample_picture(app, label_for_sample_picture, filebrowser_text))
browse_btn.grid(row = 1, column = 1)

# Train AI button
train_ai_btn = Button(buttons_frame, text = "Train AI", height = 2, width = 20, command = lambda : train_ai())
train_ai_btn.grid(row = 2, column = 1, pady = 20)

# Guess sample button
guess_sample_btn = Button(buttons_frame, text = "Ask Jin Yang", height = 2, width = 20, command = lambda : single_prediction(filebrowser_text, prediction_text))
guess_sample_btn.grid(row = 3, column = 1, pady = 20)

# Start program
app.mainloop()
    