import numpy
import matplotlib.pyplot as plt
from PIL import Image
import glob
from scipy import stats
from skimage import restoration
from skimage import exposure
from skimage import segmentation
from skimage import morphology

# Trying out: http://emmanuelle.github.io/segmentation-of-3-d-tomography-images-with-python-and-scikit-image.html

# List files and merge into 3d array
filelist = glob.glob('../data/individualTIFs/z-scan_z*c2_ORG.tif')
imgs = []
for img_path in filelist:
    im = Image.open(img_path)
    imarray = numpy.array(im)
    imgs.append(imarray)

im3d = numpy.array(imgs)
im3d.shape

# Show image for one slice
plt.imshow(im3d[50], cmap='gray')
plt.colorbar()
plt.show()

# Write cropped image in tsv
im3d_crop = im3d[:, 800:900, 700:800]
im3d_crop = im3d
plt.imshow(im3d_crop[50], cmap='gray')
plt.colorbar()
plt.show()

outf = open("../data/zscan3d-c2-gt1500.tsv", "w")
for (z, y, x), v in numpy.ndenumerate(im3d_crop):
    if(v > 1500):
        outf.write(str(x) + '\t' + str(y) + '\t' + str(z) + '\t' + str(v) + '\n')
outf.close()

# Saturate 0.5%
vmin, vmax = stats.scoreatpercentile(im3d, (0.5, 99.5))
im3d005 = numpy.clip(im3d, vmin, vmax)
im3d005 = (im3d005 - vmin) / (vmax - vmin)

plt.imshow(im3d005[50], cmap='gray')
plt.colorbar()
plt.show()

# Saturate 5%
vmin, vmax = stats.scoreatpercentile(im3d, (5, 95))
im3d05 = numpy.clip(im3d, vmin, vmax)
im3d05 = (im3d05 - vmin) / (vmax - vmin)

plt.imshow(im3d05[50], cmap='gray')
plt.colorbar()
plt.show()

# Non-local means and total-variation denoising
nlm = restoration.denoise_nl_means(im3d005[:, 800:900, 700:800],
                                   patch_size=5, patch_distance=7,
                                   h=0.12, multichannel=False)

# Look at histogram and choose threshold
hi_nlm = exposure.histogram(nlm)
plt.plot(hi_nlm[1], hi_nlm[0])
plt.show()

markers = numpy.zeros(nlm.shape, dtype=numpy.uint8)
markers[nlm > 0.1] = 1
markers[nlm < 0.05] = 2

plt.imshow(markers[50], cmap='gray')
plt.show()

# Segmentation
rw = segmentation.random_walker(nlm, markers, beta=1000., mode='cg_mg')

plt.imshow(nlm[50], cmap='gray')
plt.contour(rw[50], [1.5])
plt.show()

# Same without the slow denoising
im3d005c = im3d005[:, 600:, 600:]
hi_exp = exposure.histogram(im3d005c)
plt.plot(hi_exp[1], hi_exp[0])
plt.show()

markers = numpy.zeros(im3d005c.shape, dtype=numpy.uint8)
markers[im3d005c > 0.05] = 1
markers[im3d005c < 0.03] = 2
rw = segmentation.random_walker(im3d005c, markers, beta=10., mode='cg_mg')
# ws = morphology.watershed(im3d005c, markers)

plt.imshow(im3d005c[50], cmap='gray')
plt.contour(rw[50], [1.5])
plt.show()

# Remove small components
clean_segmentation = morphology.remove_small_objects(rw == 1, 10000)

plt.imshow(im3d005c[50], cmap='gray')
plt.contour(rw[50], [1.5])
plt.contour(clean_segmentation[50])
plt.show()

plt.imshow(clean_segmentation[50], cmap='gray')
plt.show()


# Measure connected components
from skimage import measure
labels = measure.label(clean_segmentation, background=0)
labels.max()
unique, counts = numpy.unique(labels, return_counts=True)
dict(zip(unique, counts))

lprops = measure.regionprops(labels)
lprops[0].area

skel = morphology.skeletonize_3d(clean_segmentation)
skel_labels = measure.label(skel, background=0)
skel_labels.max()
skel_props = measure.regionprops(skel_labels)
skel_props[0].area

import pickle
pickle.dump(skel, open("skel.pkl", "wb"))


# Transform into graph
import travelSkel

skel = pickle.load(open("skel.pkl", "rb"))

plt.imshow(skel[50], cmap='gray')
plt.show()

import viz3d

unique, counts = numpy.unique(skel, return_counts=True)

viz3d.plotSkel(skel)

skel = skel / skel.max()
# ep = travelSkel.endPoints(skel)
# skelp = travelSkel.pruning(skel, 10)
fils = travelSkel.travelSkel(skel)

n = [x['n'] for x in fils]
plt.hist(n)
plt.show()

pickle.dump(fils, open("fils.pkl", "wb"))
fils = pickle.load(open("fils.pkl", "rb"))

for fil in fils:
    if(fil['n'] < 10):
        skel = travelSkel.pruneFil(skel, fil)

fils = travelSkel.travelSkel(skel)

n = [x['n'] for x in fils]
plt.hist(n)
plt.show()


# Print slices for debug
for i in range(0, 107, 5):
    plt.imshow(skel[i], cmap='gray')
    plt.savefig('test' + str(i) + '.jpg')
    plt.close()


# Play with parameters
markers = numpy.zeros(im3d005c.shape, dtype=numpy.uint8)
markers[im3d005c > 0.05] = 1
markers[im3d005c < 0.03] = 2
rw = segmentation.random_walker(im3d005c, markers, beta=10., mode='cg_mg')
clean_segmentation = morphology.remove_small_objects(rw == 1, 10000)
skel = morphology.skeletonize_3d(clean_segmentation)
ep = travelSkel.endPoints(skel)
npos = numpy.where(ep > 0)
