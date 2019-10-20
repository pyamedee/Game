# -*- coding:Utf-8 -*-

from PIL import Image
from glob import glob
import numpy as np
import os


def combine(a1, a2, coef):
    #  combination seulement aux endroits ou les deux sont opaques
    b1 = a1[:, :, 3] != 0
    b2 = a2[:, :, 3] != 0
    new_array = np.zeros(a1.shape, dtype=np.uint8) + 255
    new_array[:, :, 3] = 0
    c1, c2 = (b1 & b2).nonzero()  # indices ou les deux sont opaques
    d1, d2 = (b1 != b2).nonzero()
    for x, y in zip(c1, c2):
        new_array[x, y] = np.array(a1[x, y] * (1 - coef) + a2[x, y] * coef)

    for x, y in zip(d1, d2):
        if a1[x, y, 3] != 0:
            new_array[x, y, 3] = np.array(a1[x, y, 3] * (1 - coef))
            new_array[x, y, :3] = np.array(a1[x, y, :3])
        else:
            new_array[x, y, 3] = np.array(a2[x, y, 3] * coef)
            new_array[x, y, :3] = np.array(a2[x, y, :3])

    return new_array


path = r'C:\Users\Hélène Le Berre\rp\Game\ResourcesBase\Entity\Rogue\Attack'

img_list = list()
img1 = None
img2 = None
for img_path in glob(path + '\\*.png'):
    img2 = img1
    img1 = Image.open(img_path)

    if img2 is not None:
        tab1 = np.array(img1)
        tab2 = np.array(img2)
        tab_inter1 = combine(tab1, tab2, 0.66)
        tab_inter2 = combine(tab1, tab2, 0.33)
        # tab_inter3 = combine(tab1, tab2, 0.25)
        img_list.append(Image.fromarray(tab_inter1))
        img_list.append(Image.fromarray(tab_inter2))
        # img_list.append(Image.fromarray(tab_inter3))
    img_list.append(img1)

os.mkdir('C:\\Users\\Hélène Le Berre\\rp\\Game\\Resources\\Entity\\Rogue\\Attack2')
for i, image in enumerate(img_list):
    image.save(f'C:\\Users\\Hélène Le Berre\\rp\\Game\\Resources\\Entity\\Rogue\\Attack2\\Attack{i:0>2}.png')

