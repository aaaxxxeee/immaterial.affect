from PIL import Image
import random

# Load image with alpha channel
img = Image.open("hdd/igprofile.png").convert("RGBA")
pixels = img.load()

width, height = img.size

# Adjust the probability (0.0 to 1.0)
delete_chance = 0.05  # 5% chance to "delete" a pixel

for y in range(height):
    for x in range(width):
        if random.random() < delete_chance:
            r, g, b, a = pixels[x, y]
            pixels[x, y] = (r, g, b, 0)  # transparent pixel

# Save to a new file (PNG supports alpha)
img.save("hdd/igprofile.png")
