import random
from PIL import Image, ImageDraw, ImageFont
import os

path = "./"
file_list = os.listdir(path)
file_list = [file for file in file_list if file.endswith(".jpg")]

for i in file_list:

    img = Image.open(i).convert("RGBA")
    file_name=os.path.basename(i)
    
    txt = Image.new('RGBA', img.size, (255,255,255,0))
 
    text = "noexpect.tistory.com"
    font = ImageFont.truetype("arial.ttf",int(min(img.size)/10))

    d = ImageDraw.Draw(txt)

    width, height = img.size 
    textwidth, textheight = d.textsize(text, font)
    x=width/2-textwidth/2
    y=height/2-textheight/2

    d.text((x,y), text, fill=(255,255,255,150), font=font)

    watermarked = Image.alpha_composite(img, txt)
    
    watermarked.save(file_name+'.png')
