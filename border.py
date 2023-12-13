### 이미지 외곽에 테두리를 만듦 ### 

from PIL import Image

def apply_shadow(image_path, alpha, thickness):

    img = Image.open(image_path)

    shadow = Image.new("RGBA", (thickness,img.height), (0, 0, 0, int(255 * alpha)))
    img.paste(shadow, (0, 0), shadow)

    shadow = Image.new("RGBA", (img.width,thickness), (0, 0, 0, int(255 * alpha)))
    img.paste(shadow, (thickness, 0), shadow)
   
    shadow = Image.new("RGBA", (img.width,thickness), (0, 0, 0, int(255 * alpha)))
    img.paste(shadow, (thickness, img.height-thickness), shadow)

    shadow = Image.new("RGBA", (thickness, img.height-thickness*2), (0, 0, 0, int(255 * alpha)))
    img.paste(shadow, (img.width-thickness, thickness), shadow)

    return img

shadowed_img = apply_shadow("image.jpg", 0.15, 1)

shadowed_img.show()
