import numpy
from PIL import Image
import glob
from scipy import stats
from skimage import segmentation
from skimage import morphology
import travelSkel
import matplotlib.pyplot as plt

filelist = glob.glob('../data/individualTIFs/z-scan_z*c2_ORG.tif')
imgs = []
for img_path in filelist:
    im = Image.open(img_path)
    imarray = numpy.array(im)
    imgs.append(imarray)

im3d = numpy.array(imgs)
vmin, vmax = stats.scoreatpercentile(im3d, (0.5, 99.5))
im3d005 = numpy.clip(im3d, vmin, vmax)
im3d005 = (im3d005 - vmin) / (vmax - vmin)

im2d = im3d005[50]
plt.imshow(im2d, cmap='gray')
plt.show()

markers = numpy.zeros(im2d.shape, dtype=numpy.uint8)
markers[im2d > 0.2] = 1
markers[im2d < 0.04] = 2
rw = segmentation.random_walker(im2d, markers, beta=100., mode='cg_mg')
clean_segmentation = morphology.remove_small_objects(rw == 1, 10000)

plt.imshow(im2d, cmap='gray')
plt.contour(rw, [1.5])
plt.contour(clean_segmentation)
plt.show()

skel = morphology.skeletonize_3d(clean_segmentation)

plt.imshow(skel, cmap='gray')
plt.contour(rw, [1.5])
plt.contour(clean_segmentation)
plt.show()

medial = morphology.medial_axis(clean_segmentation)

plt.imshow(medial, cmap='gray')
plt.contour(rw, [1.5])
plt.contour(clean_segmentation)
plt.show()


import viz3d

viz3d.plotSkel(skel)

ep = travelSkel.endPoints(skel)
nep = numpy.where(ep > 0)

from skimage.draw import ellipse

img = numpy.zeros((50, 50, 50), dtype=numpy.uint8)
rr, cc = ellipse(25, 25, 3, 25)
img[14:16, rr, cc] = 1
rr, cc = ellipse(25, 25, 25, 3)
img[12:22, rr, cc] = 1
viz3d.plotSkel(img)

skel = morphology.skeletonize_3d(img)
viz3d.plotSkel(skel)
