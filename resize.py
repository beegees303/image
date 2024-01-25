#특정폴더를 선택해 그 폴더 안의 이미지 파일의 해상도를 모두 바꾼다. 

from PIL import Image
import os

def resize_images(folder_path, new_width, new_height):

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            filepath = os.path.join(folder_path, filename)
            with Image.open(filepath) as image:
                new_width = new_width  # Maintain aspect ratio while resizing
                new_height = new_height
                image = image.resize((new_width, new_height), Image.ANTIALIAS)
                image.save(filepath)


from tkinter import filedialog

directory_path = filedialog.askdirectory(
    title="Select a Directory",
)

new_width=int(input("Please enter width : "))
new_height=int(input("Please enter height : "))


resize_images(directory_path, new_width, new_height)
