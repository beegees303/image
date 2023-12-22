try:
    ConsoleThick=int(input("Please enter border thickness(default value=1) : "))
except:
    ConsoleThick=1

try:
    ConsoleAlpha=float(input("Please enter alpha value(default value=1) : "))
except:
    ConsoleAlpha=1

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    r, g, b = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    return r, g, b

ConsoleRGB=input("Please enter RGB hexcode(default value=black) : ")
if ConsoleRGB=="":
    ConsoleRGB="#000000"

r,g,b=hex_to_rgb(ConsoleRGB)

import tkinter as tk
from tkinter import filedialog

root=tk.Tk()
root.withdraw() ## tk root window를 숨깁니다. 

filename=filedialog.askopenfilename(title = "Select image file",filetypes = [("image file","*.jpg;*.png")] )

pdfFileObj = open(filename, 'rb')

from PIL import Image

def apply_shadow(image_path, alpha, thickness):

    img = Image.open(image_path)

    shadow = Image.new("RGBA", (thickness,img.height), (r, g, b, int(255 * alpha)))
    img.paste(shadow, (0, 0), shadow)

    shadow = Image.new("RGBA", (img.width,thickness), (r, g, b, int(255 * alpha)))
    img.paste(shadow, (thickness, 0), shadow)
   
    shadow = Image.new("RGBA", (img.width,thickness), (r, g, b, int(255 * alpha)))
    img.paste(shadow, (thickness, img.height-thickness), shadow)

    shadow = Image.new("RGBA", (thickness, img.height-thickness*2), (r, g, b, int(255 * alpha)))
    img.paste(shadow, (img.width-thickness, thickness), shadow)

    return img

shadowed_img = apply_shadow(pdfFileObj, ConsoleAlpha, ConsoleThick)

shadowed_img.show()

