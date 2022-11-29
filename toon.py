garosize=378 #웹툰 그림 너비
yb=100 #그림 간 여백
colr=(255,255,255) #여백 색깔 RGB 코드 


import os

path = "./"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".PNG") or file.endswith(".png") or file.endswith(".JPG") or file.endswith("jpg")]

from PIL import Image

serosize=0
seropos=0

for i in file_list_py:
    img=Image.open(i)
    serosize=serosize+img.size[1]+yb

new_image = Image.new('RGB',(garosize, serosize), colr)

for i in file_list_py:
    img=Image.open(i)
    img=img.resize((garosize,img.size[1]))
    new_image.paste(img,(0,seropos))
    seropos=seropos+yb
    seropos=seropos+img.size[1]

new_image.save("toon.jpg","JPEG")