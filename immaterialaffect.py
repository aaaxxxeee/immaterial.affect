from PIL import Image

threshold = 0

image_file = Image.open("hdd/igprofile.png")
# Grayscale
image_file = image_file.convert('L')
# Threshold
image_file = image_file.point( lambda p: 255 if p > threshold else 0 )
# To mono
image_file = image_file.convert('1')

Image.save("hdd/outfile.png")