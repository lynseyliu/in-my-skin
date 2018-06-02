from scipy import ndimage, misc
import numpy as np
import os

root_dir = './data/train/malignant'
for i in range(1, 4):
    for filename in os.listdir(root_dir):
        image = os.path.join(root_dir, filename)
        print(image)
        image_to_rotate = ndimage.imread(image)
        rotated = ndimage.rotate(image_to_rotate, 45 * i)
        fullpath = os.path.join(root_dir + str(i), 'rotated_' + filename)
        misc.imsave(fullpath, rotated)
