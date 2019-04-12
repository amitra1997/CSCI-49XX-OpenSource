import numpy as np
import PIL
from PIL import Image
from PIL import ImageOps

def imageModify(imgName):
    img = Image.open('lab11pics/' + imgName + '.jpg')
    img = img.resize((28, 28))
    img = img.convert('L')
    img = ImageOps.invert(img)
    img.save('lab11pics/' + imgName + 'Mod.jpg', 'JPEG')

imageModify('coat')
imageModify('shirt')
imageModify('shoe')