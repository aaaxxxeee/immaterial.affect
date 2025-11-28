# lib
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import random, os
import pyautogui

def convert_jpgs_to_pngs(folder):
    for r, _, fs in os.walk(folder):
        for f in fs:
            if f.lower().endswith(('.jpg', '.jpeg')):
                p = os.path.join(r, f)
                im = Image.open(p).convert('RGBA')
                out = os.path.splitext(p)[0] + '.png'
                im.save(out, 'PNG')
                im.close()
                os.remove(p)

def decompose(p,portion=1,o=None):
    i = Image.open(p)
    px = i.load(); w, h = i.size
    for y in range(h):
        for x in range(w):
            if random.random() < portion:
                val = px[x, y]
                if len(val) == 4:
                    r, g, b, a = val; px[x, y] = (r, g, b, 0)
                else:
                    r, g, b = val; px[x, y] = (r, g, b)
    i.save(o or p)
    
if __name__ == '__main__':
    convert_jpgs_to_pngs('hdd')
    while True:
        for r, _, fs in os.walk('hdd'):
            for f in fs:
                if f.lower().endswith('.png'):
                    decompose(os.path.join(r, f), portion=0.05)
                    print("memory deterioration in progress on " + str(f))
                    #pyautogui.write('chafa '+ str(f))
                    #pyautogui.press('enter')
                    #pyautogui.write('clear')
                    #pyautogui.press('enter')