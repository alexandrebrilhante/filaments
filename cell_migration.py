import math
import os
import matplotlib.pyplot as plt
import numpy as np
from skimage import data, io
from skimage.feature import canny
from skimage.measure import label, regionprops
from skimage.transform import (hough_line, hough_line_peaks, probabilistic_hough_line)
from skimage.util import img_as_bool

image = img_as_bool(io.imread("cell.tif", as_grey=True)+0.15)

edges = canny(image)

label_img = label(edges)
regions = regionprops(label_img)

fig, ax = plt.subplots()
ax.imshow(edges, cmap=plt.cm.gray)

for props in regions:
    y0, x0 = props.centroid
    orientation = props.orientation
    x1 = x0 + math.cos(orientation) * 0.5 * props.major_axis_length
    x0 = x0 - math.cos(orientation) * 0.5 * props.major_axis_length
    y1 = y0 - math.sin(orientation) * 0.5 * props.major_axis_length
    y0 = y0 + math.sin(orientation) * 0.5 * props.major_axis_length

    # reference: http://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops
    print "Length: ", props.major_axis_length
    print "Orientation [-pi/2, pi/2]: ", orientation
    print "Area (pixs): ", props.area
    
    ax.plot((x0, x1), (y0, y1), '-r', linewidth=1.5)

fig.tight_layout()
plt.show()