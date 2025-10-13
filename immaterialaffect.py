# lib
from PIL import Image
import random
import os

def decompose(img_path, portiontodelete=1, output_path=None):

# ouvrir image
    img = Image.open(img_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            if random.random() < portiontodelete:
                r, g, b, a = pixels[x, y]
                pixels[x, y] = (r, g, b, 0)  # transparent pixel

# save
    if not output_path:
        output_path = image_path 
    img.save(output_path)

decompose("hdd/igprofile.png", portiontodelete=1, output_path="hdd/igprofile.png")