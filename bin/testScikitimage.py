import numpy
import matplotlib.pyplot as plt
from PIL import Image
import glob
from scipy import stats
from skimage import restoration

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
plt.imshow(im3d_crop[50], cmap='gray')
plt.colorbar()
plt.show()

outf = open("../data/zscan3d-c2-crop-x700_800-y800_900.tsv", "w")
for (z, y, x), v in numpy.ndenumerate(im3d_crop):
    if(v != 0):
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
