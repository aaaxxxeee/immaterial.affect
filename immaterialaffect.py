# lib
from PIL import Image
import random, os

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

while True:
    for r,_,fs in os.walk('hdd'):
        for f in fs:
            if f.lower().endswith(('.png','.jpg','.jpeg')):
                decompose(os.path.join(r,f),portion=0.05)
                print("memory deterioration in progress on " + str(f))