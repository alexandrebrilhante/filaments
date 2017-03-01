import numpy
from PIL import Image
import glob
from scipy import stats
from skimage import segmentation
from skimage import morphology
import travelSkel
import viz3d
import matplotlib.pyplot as plt
import pickle

filelist = glob.glob('../data/individualTIFs/z-scan_z*c2_ORG.tif')
imgs = []
for img_path in filelist:
    im = Image.open(img_path)
    im = im.resize((600, 600))
    imarray = numpy.array(im)
    imgs.append(imarray)

im3d = numpy.array(imgs)
vmin, vmax = stats.scoreatpercentile(im3d, (0.5, 99.5))
im3d005 = numpy.clip(im3d, vmin, vmax)
im3d005 = (im3d005 - vmin) / (vmax - vmin)
# im3d005 = im3d005[:, 400:, 400:]

outf = open("../data/zscan3d-c2-gt1500.tsv", "w")
for (z, y, x), v in numpy.ndenumerate(im3d):
    if(v > 1500):
        outf.write(str(x) + '\t' + str(y) + '\t' + str(z) + '\t' + str(v) + '\n')
outf.close()


plt.imshow(im3d005[50], cmap='gray')
plt.colorbar()
plt.show()

markers = numpy.zeros(im3d005.shape, dtype=numpy.uint8)
markers[im3d005 > 0.2] = 1
markers[im3d005 < 0.02] = 2
rw = segmentation.random_walker(im3d005, markers, beta=10., mode='cg_mg')

pickle.dump(rw, open("rw.pkl", "wb"))
rw = pickle.load(open("rw.pkl", "rb"))

clean_segmentation = morphology.remove_small_objects(rw == 1, 10000)

plt.imshow(im3d005[50], cmap='gray')
plt.contour(rw[50], [1.5])
plt.contour(clean_segmentation[50])
plt.show()

plt.imshow(clean_segmentation[50], cmap='gray')
plt.show()

skel = morphology.skeletonize_3d(clean_segmentation)

pickle.dump(skel, open("skel.pkl", "wb"))
skel = pickle.load(open("skel.pkl", "rb"))

plt.imshow(skel[50], cmap='gray')
plt.contour(rw[50], [1.5])
plt.contour(clean_segmentation[50])
plt.show()

viz3d.plotSkel(skel)

skel2d = morphology.skeletonize_3d(clean_segmentation[50])
plt.imshow(skel2d, cmap='gray')
plt.contour(clean_segmentation[50])
plt.show()

skel = skel / skel.max()
# ep = travelSkel.endPoints(skel)
# skelp = travelSkel.pruning(skel, 10)
fils = travelSkel.travelSkel(skel)

n = [x['n'] for x in fils]
plt.hist(n)
plt.xlabel('filament length (pixel)')
plt.ylabel('number of filaments')
plt.show()

pickle.dump(fils, open("fils.pkl", "wb"))
fils = pickle.load(open("fils.pkl", "rb"))

for fil in fils:
    if(fil['n'] < 10):
        skel = travelSkel.pruneFil(skel, fil)

pickle.dump(skel, open("skel2.pkl", "wb"))
skel = pickle.load(open("skel2.pkl", "rb"))

fils = travelSkel.travelSkel(skel)

n2 = [x['n'] for x in fils]
plt.hist(n2)
plt.xlabel('filament length (pixel)')
plt.ylabel('number of filaments')
plt.show()

l2 = [x['length'] for x in fils]
plt.hist(l2)
plt.xlabel('filament length (um)')
plt.ylabel('number of filaments')
plt.show()

outf = open("../data/zscan3d-c2-skeleton.tsv", "w")
for (z, y, x), v in numpy.ndenumerate(skel):
    if(v > 0):
        outf.write(str(x) + '\t' + str(y) + '\t' + str(z) + '\t' + str(v) + '\n')
outf.close()
