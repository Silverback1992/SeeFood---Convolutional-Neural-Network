# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:46:10 2020

@author: alin2
"""
from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
from io import BytesIO
from tkinter import filedialog
import h5py

def get_sample_picture(app, l, txt_box):
    picture_path = browse_files(app, txt_box)
    display_sample(app, l, picture_path)

def browse_files(app, txt_box):
    txt_box.configure(state = "normal")
    
    txt_box.delete("1.0", END)
    
    selected_file = open_file(app)
    txt_box.insert("1.0", selected_file)

    txt_box.configure(state = "disabled")
    
    return selected_file

def display_sample(app, l, pic_path):
    img = Image.open(pic_path)
    img = img.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img, master = app)
    l.configure(image=photo)
    l.image = photo # this line need to prevent gc
    
def open_file(app):
    selected_file = filedialog.askopenfilenames(
        parent=app,
    	initialdir=os.path.dirname(os.path.abspath(__file__)),
    	filetypes=[
            ("PNG", "*.png"),
            ("JPG", "*.jpg"),
            ])
    return selected_file[0]
