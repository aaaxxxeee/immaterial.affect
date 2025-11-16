# lib
from PIL import Image
import random, os

def decompose(p,portion=1,o=None):
    i=Image.open(p).convert('RGBA');px=i.load();w,h=i.size
    for y in range(h):
        for x in range(w):
            if random.random()<portion:
                r,g,b,a=px[x,y];px[x,y]=(r,g,b,0)
    i.save(o or p)

while True:
    for r,_,fs in os.walk('hdd'):
        for f in fs:
            if f.lower().endswith(('.png','.jpg','.jpeg')):
                decompose(os.path.join(r,f),portion=0.05)