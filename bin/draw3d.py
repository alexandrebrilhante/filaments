from skimage.draw import ellipse
from skimage.draw import ellipsoid
import numpy as np
import viz3d

img = np.zeros((20, 20), dtype=np.uint8)
rr, cc = ellipse(10, 10, 2, 7)
img[rr, cc] = 1
rr, cc = ellipse(10, 10, 7, 2)
img[rr, cc] = 1
img

