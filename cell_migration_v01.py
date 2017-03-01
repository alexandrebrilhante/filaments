farzuntu@farzInspiron-5547:~/Coding/biohackethon$ PS1="\u "
farzuntu python cell_migration.py
Traceback (most recent call last):
  File "cell_migration.py", line 11, in <module>
    from czifile import CziFile
ImportError: No module named czifile
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 55, in <module>
    ax2 = fig.add_subplot(1, 3, 2, projection='3d', sharex=ax1, sharey=ax1)
NameError: name 'ax1' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 57, in <module>
    point_y_s, point_x_s = np.where(np.abs(s_smooth - target) < delta)
NameError: name 'np' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 70, in <module>
    ax1.scatter(point_x, point_y, color='blue', **scatter_settings)
NameError: name 'point_x' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python plot_random_walker_segmentation.py 
farzuntu python plot_random_walker_segmentation.py 
Traceback (most recent call last):
  File "plot_random_walker_segmentation.py", line 36, in <module>
    image = img_as_bool(io.imread("cell.tif", as_grey=True))
NameError: name 'img_as_bool' is not defined
farzuntu python plot_random_walker_segmentation.py 
Traceback (most recent call last):
  File "plot_random_walker_segmentation.py", line 39, in <module>
    markers = np.zeros(data.shape, dtype=np.uint)
NameError: name 'data' is not defined
farzuntu python plot_random_walker_segmentation.py 
Traceback (most recent call last):
  File "plot_random_walker_segmentation.py", line 40, in <module>
    markers = np.zeros(data.shape, dtype=np.uint)
NameError: name 'data' is not defined
farzuntu python plot_random_walker_segmentation.py 
Traceback (most recent call last):
  File "plot_random_walker_segmentation.py", line 45, in <module>
    labels = random_walker(data, markers, beta=10, mode='bf')
  File "/home/farzuntu/.local/lib/python2.7/site-packages/skimage/segmentation/random_walker_segmentation.py", line 453, in random_walker
    return_full_prob=return_full_prob)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/skimage/segmentation/random_walker_segmentation.py", line 480, in _solve_bf
    X = np.argmax(X, axis=0)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/numpy/core/fromnumeric.py", line 963, in argmax
    return _wrapfunc(a, 'argmax', axis=axis, out=out)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/numpy/core/fromnumeric.py", line 57, in _wrapfunc
    return getattr(obj, method)(*args, **kwds)
ValueError: attempt to get argmax of an empty sequence
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 31, in <module>
    ax[1].imshow(dist_on_skel, cmap=magma, interpolation='nearest')
NameError: name 'magma' is not defined
farzuntu python cell_migration.py
Traceback (most recent call last):
  File "cell_migration.py", line 11, in <module>
    from skimage.util.colormap import magma
ImportError: cannot import name magma
farzuntu python cell_migration.py
Traceback (most recent call last):
  File "cell_migration.py", line 11, in <module>
    from skimage.util.colormap import magma
ImportError: cannot import name magma
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 32, in <module>
    ax[1].imshow(dist_on_skel, cmap=blue, interpolation='nearest')
NameError: name 'blue' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 32, in <module>
    ax[1].imshow(dist_on_skel, cmap=plt.cm.blue, interpolation='nearest')
AttributeError: 'module' object has no attribute 'blue'
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 33, in <module>
    ax[1].contour(data, [0.5], colors='w')
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/__init__.py", line 1892, in inner
    return func(ax, *args, **kwargs)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/axes/_axes.py", line 5819, in contour
    contours = mcontour.QuadContourSet(self, *args, **kwargs)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/contour.py", line 864, in __init__
    self._process_args(*args, **kwargs)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/contour.py", line 1429, in _process_args
    x, y, z = self._contour_args(args, kwargs)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/contour.py", line 1504, in _contour_args
    z = ma.asarray(args[0], dtype=np.float64)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/numpy/ma/core.py", line 7652, in asarray
    subok=False, order=order)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/numpy/ma/core.py", line 2766, in __new__
    order=order, subok=True, ndmin=ndmin)
TypeError: float() argument must be a string or a number
farzuntu python3 cell_migration.py
Traceback (most recent call last):
  File "cell_migration.py", line 8, in <module>
    from skimage.morphology import skeletonize, skeletonize_3d, medial_axis
ImportError: cannot import name 'skeletonize_3d'
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 33, in <module>
    ax[1].contour(data, [0.5], colors='w')
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/__init__.py", line 1892, in inner
    return func(ax, *args, **kwargs)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/axes/_axes.py", line 5819, in contour
    contours = mcontour.QuadContourSet(self, *args, **kwargs)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/contour.py", line 864, in __init__
    self._process_args(*args, **kwargs)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/contour.py", line 1429, in _process_args
    x, y, z = self._contour_args(args, kwargs)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/matplotlib/contour.py", line 1504, in _contour_args
    z = ma.asarray(args[0], dtype=np.float64)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/numpy/ma/core.py", line 7652, in asarray
    subok=False, order=order)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/numpy/ma/core.py", line 2766, in __new__
    order=order, subok=True, ndmin=ndmin)
TypeError: float() argument must be a string or a number
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 41, in <module>
    ax[3].imshow(skeleton3d, cmap=plt.cm.gray, interpolation='nearest')
IndexError: index 3 is out of bounds for axis 0 with size 3
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 20, in <module>
    skel, distance = medial_axis(data, return_distance=True)
  File "/home/farzuntu/.local/lib/python2.7/site-packages/skimage/morphology/_skeletonize.py", line 176, in medial_axis
    masked_image = image.astype(np.bool)
AttributeError: 'module' object has no attribute 'astype'
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 43, in <module>
    elevation_map = sobel(image)
NameError: name 'sobel' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 55, in <module>
    for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
NameError: name 'h' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 28, in <module>
    print dtype_limits(image)
NameError: name 'dtype_limits' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
(0, True)
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
(0, 1)
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
(0, 1)
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
(0, 1)
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 80, in <module>
    label_img = label(image)
NameError: name 'label' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
Traceback (most recent call last):
  File "cell_migration.py", line 91, in <module>
    x1 = x0 + math.cos(orientation) * 0.5 * props.major_axis_length
NameError: name 'math' is not defined
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e85f90>
164.700368072
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e85110>
25.2204069809
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b310>
4.78091443734
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b350>
141.016932381
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b390>
300.474033473
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b3d0>
23.0586141146
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b410>
11.8385688082
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b450>
452.624760364
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b490>
15.2081861606
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b4d0>
25.6260894133
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b510>
3.70328039909
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b550>
6.51232309436
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b590>
3.46410161514
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b5d0>
3.46410161514
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b610>
5.25339229803
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b650>
12.2653657244
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b690>
5.25339229803
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b6d0>
3.46410161514
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b710>
141.620068041
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b750>
21.4097173979
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b790>
3.46410161514
<skimage.measure._regionprops._RegionProperties object at 0x7faab3e9b7d0>
3.46410161514
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
164.700368072
25.2204069809
4.78091443734
141.016932381
300.474033473
23.0586141146
11.8385688082
452.624760364
15.2081861606
25.6260894133
3.70328039909
6.51232309436
3.46410161514
3.46410161514
5.25339229803
12.2653657244
5.25339229803
3.46410161514
141.620068041
21.4097173979
3.46410161514
3.46410161514
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
164.700368072 0.61573530056
25.2204069809 0.747350131656
4.78091443734 0.785398163397
141.016932381 1.24720842973
300.474033473 1.3825563156
23.0586141146 -0.176368421747
11.8385688082 -0.373332193318
452.624760364 -1.29327403714
15.2081861606 0.788169670593
25.6260894133 -1.32852444571
3.70328039909 -0.785398163397
6.51232309436 -0.44423988596
3.46410161514 0.785398163397
3.46410161514 0.785398163397
5.25339229803 0.181573504973
12.2653657244 -1.29201123105
5.25339229803 -0.181573504973
3.46410161514 0.785398163397
141.620068041 -0.181745997625
21.4097173979 -0.36928312692
3.46410161514 0.785398163397
3.46410161514 0.785398163397
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
164.700368072 0.61573530056
25.2204069809 0.747350131656
4.78091443734 0.785398163397
141.016932381 1.24720842973
300.474033473 1.3825563156
23.0586141146 -0.176368421747
11.8385688082 -0.373332193318
452.624760364 -1.29327403714
15.2081861606 0.788169670593
25.6260894133 -1.32852444571
3.70328039909 -0.785398163397
6.51232309436 -0.44423988596
3.46410161514 0.785398163397
3.46410161514 0.785398163397
5.25339229803 0.181573504973
12.2653657244 -1.29201123105
5.25339229803 -0.181573504973
3.46410161514 0.785398163397
141.620068041 -0.181745997625
21.4097173979 -0.36928312692
3.46410161514 0.785398163397
3.46410161514 0.785398163397
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
214.732876297 0.653779070154
3.46410161514 0.785398163397
3.46410161514 0.785398163397
16.3572118258 0.810138030637
3.46410161514 0.785398163397
115.466859894 -0.786637787437
3.46410161514 0.785398163397
129.539955807 1.55047637076
14.1421356237 0.785398163397
29.3426928919 -0.498776151148
413.383344452 -1.2741312037
22.8762966802 1.23918948456
3.70328039909 -0.785398163397
8.48528137424 -0.0
14.1421356237 0.785398163397
43.1452066877 -0.609972280676
3.46410161514 0.785398163397
6.02757212765 0.162617430427
3.46410161514 0.785398163397
3.46410161514 0.785398163397
9.7790378094 1.12573407316
17.9021150803 0.550733062875
3.46410161514 0.785398163397
21.7060392396 0.234284014904
12.4091521715 0.333413185393
20.6053463498 -0.155681073167
3.46410161514 0.785398163397
3.70328039909 -0.785398163397
11.4646114746 -0.158226788201
12.9154990762 0.280739543027
3.26598632371 -1.57079632679
2.0 -1.57079632679
4.73286382648 -1.57079632679
15.7704116101 0.785398163397
25.6091704141 -0.24988795133
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
125.895109131 0.613428963853
3.46410161514 0.785398163397
32.9740563066 1.54583302614
3.46410161514 -0.0
8.1929748235 0.459590902886
2.0 0.785398163397
10.5078026909 0.377072479866
13.7843641408 1.03885814981
3.70328039909 0.785398163397
6.44763580227 0.108130622936
38.8626242208 0.761942492676
52.9934087835 0.829988185861
6.84375679928 1.06683227982
6.14630682799 0.840294621974
4.46409815432 0.819436392526
7.2506157374 -1.57079632679
3.70328039909 -0.785398163397
15.297715489 1.47721210021
10.7594488352 1.23009407757
13.9302838351 0.866862678061
262.819664851 -0.667475162005
24.8416675082 0.668029191807
3.46410161514 -1.57079632679
31.4368697403 0.102624979119
8.11602466285 -0.241723500784
87.0048390772 0.917919701729
3.46410161514 -0.0
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
155.41413983 0.61182400465
3.46410161514 -1.57079632679
73.6821521535 1.17230335915
133.063229519 0.656614798136
7.05816530493 1.49379886641
3.46410161514 -0.0
20.0115217307 0.907572110075
63.5067220329 1.45797980015
3.46410161514 0.785398163397
251.749246382 -0.563278465522
19.5295180644 -0.416083895729
4.73286382648 -0.0
7.82504337486 -0.986268528854
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
164.700368072 0.61573530056
25.2204069809 0.747350131656
4.78091443734 0.785398163397
141.016932381 1.24720842973
300.474033473 1.3825563156
23.0586141146 -0.176368421747
11.8385688082 -0.373332193318
452.624760364 -1.29327403714
15.2081861606 0.788169670593
25.6260894133 -1.32852444571
3.70328039909 -0.785398163397
6.51232309436 -0.44423988596
3.46410161514 0.785398163397
3.46410161514 0.785398163397
5.25339229803 0.181573504973
12.2653657244 -1.29201123105
5.25339229803 -0.181573504973
3.46410161514 0.785398163397
141.620068041 -0.181745997625
21.4097173979 -0.36928312692
3.46410161514 0.785398163397
3.46410161514 0.785398163397
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
160.950635551 0.615340280626
12.6084004112 0.822579626974
11.7808906216 -1.41754327106
4.73286382648 -0.0
6.15812677303 0.559929948779
122.261944247 1.22681914284
3.46410161514 0.785398163397
154.112486736 0.720997789362
10.5999695823 -1.54518259949
8.87468929418 0.00204637329427
30.2341593417 0.546550368669
69.740233884 1.46077710855
3.70328039909 0.785398163397
260.015368818 -0.537057554862
4.90935409573 0.306603674437
3.46410161514 0.785398163397
49.3079620919 -0.160113674295
279.001991038 -0.199274200855
6.25973401091 1.26927165304
3.46410161514 0.785398163397
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
187.952060668 0.605952449815
0.0 0.785398163397
0.0 0.785398163397
4.472135955 -1.57079632679
15.1380865408 0.423779321109
3.26598632371 -0.0
2.0 -1.57079632679
3.26598632371 -1.57079632679
0.0 0.785398163397
140.710073187 1.22676090673
0.0 0.785398163397
2.0 -0.0
2.0 -0.0
4.49801340575 -0.115545333598
0.0 0.785398163397
11.2404511299 -0.775643303686
2.82842712475 0.785398163397
63.4853584223 -1.43560309703
0.0 0.785398163397
4.472135955 -0.0
2.82842712475 -0.785398163397
2.0 -0.0
6.62316031695 -0.553574358897
2.82842712475 -0.785398163397
2.82842712475 0.785398163397
10.7501992955 -0.734149813772
0.0 0.785398163397
36.1422423966 -0.26341741254
455.414059967 -1.36460871927
6.3400110335 0.473386636909
5.77331086476 -0.205063670271
3.67708852834 -0.491396861624
0.0 0.785398163397
0.0 0.785398163397
3.26598632371 -0.0
10.6636510405 0.228793538571
5.37850512054 1.52646838586
27.9179284431 -1.10552521955
3.26598632371 -1.57079632679
0.0 0.785398163397
2.0 -1.57079632679
3.67708852834 -0.491396861624
0.0 0.785398163397
3.26598632371 -0.0
3.26598632371 -0.0
2.82842712475 0.785398163397
0.0 0.785398163397
3.67708852834 1.07939946517
3.67708852834 -1.07939946517
14.9507350822 -0.84955977724
11.0000940876 0.408141324428
2.82842712475 -0.785398163397
2.0 -0.0
11.0860379898 -0.288021102214
7.41225373224 0.974611852412
10.2048759601 0.673659862827
17.4821098944 -0.344310532094
43.5323269496 0.222332073716
2.0 -0.0
2.0 -0.0
14.254858117 -0.571038989732
3.26598632371 -0.0
11.8291252159 0.777510468266
2.0 -1.57079632679
4.6802057672 -0.307331475961
0.0 0.785398163397
2.0 -0.0
17.6452167791 0.306298486276
5.91280935794 0.299209446739
2.0 -0.0
0.0 0.785398163397
2.0 -1.57079632679
2.0 -0.0
2.0 -0.0
0.0 0.785398163397
5.77331086476 0.205063670271
2.0 -0.0
2.0 -0.0
2.0 -1.57079632679
2.0 -0.0
42.7392160895 0.569826816775
5.49594770443 -0.9408973037
10.3687919485 0.345329997691
16.6894017072 0.245032951943
4.68651314737 1.00160205118
10.4717027737 0.166622150556
8.72157529625 0.414424529394
0.0 0.785398163397
2.0 -1.57079632679
2.0 -0.0
4.89594928386 0.366407550893
0.0 0.785398163397
2.0 -0.0
2.0 -1.57079632679
3.67708852834 -1.07939946517
32.9095058725 -0.254768120951
2.0 -0.0
5.49594770443 0.629899023095
3.67708852834 -0.491396861624
12.7113902878 0.81401271657
0.0 0.785398163397
2.82842712475 -0.785398163397
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
160.254642195 0.621355189853
0.0 0.785398163397
2.0 -0.0
2.0 -0.0
5.37398842113 0.553574358897
0.0 0.785398163397
0.0 0.785398163397
0.0 0.785398163397
3.67708852834 0.491396861624
2.0 -0.0
4.61880215352 0.785398163397
76.9697315442 1.45020233533
9.88397664026 1.24671089944
4.6802057672 1.26346485083
0.0 0.785398163397
4.61880215352 -0.785398163397
4.32440845118 0.431085027334
9.79795897113 -0.785398163397
3.26598632371 -0.0
0.0 0.785398163397
12.2658924823 0.575066488831
14.8626366576 -0.950090160355
0.0 0.785398163397
2.0 -0.0
128.202950304 0.652900874484
3.26598632371 -0.0
5.65685424949 -1.57079632679
0.0 0.785398163397
0.0 0.785398163397
5.95614635295 0.347369138098
2.82842712475 -0.785398163397
19.9778779212 -1.33602511089
2.0 -0.0
2.0 -0.0
30.4826737068 0.559696591788
4.472135955 -0.0
4.82842712475 -0.392699081699
2.0 -0.0
40.7455084887 1.0956948495
0.0 0.785398163397
3.26598632371 -1.57079632679
9.37683470923 1.01889981395
0.0 0.785398163397
3.26598632371 -0.0
285.313568291 -1.09378076269
2.0 -0.0
3.26598632371 -0.0
2.0 -1.57079632679
21.0928769051 0.630696132738
0.0 0.785398163397
3.26598632371 -0.0
32.8712543362 0.770530791381
0.0 0.785398163397
3.67708852834 -1.07939946517
3.26598632371 -0.0
5.37398842113 -1.0172219679
3.26598632371 -1.57079632679
2.0 -1.57079632679
2.0 -0.0
2.0 -1.57079632679
3.26598632371 -0.0
9.90369936542 0.392699081699
0.0 0.785398163397
2.0 -1.57079632679
0.0 0.785398163397
3.67708852834 0.491396861624
0.0 0.785398163397
6.05546037902 -0.711858985703
2.0 -0.0
0.0 0.785398163397
27.3920350109 0.665253868446
3.26598632371 -0.0
5.49594770443 -0.629899023095
2.82842712475 -0.785398163397
30.2916432106 0.139160502203
2.82842712475 0.785398163397
0.0 0.785398163397
0.0 0.785398163397
2.0 -0.0
2.0 -1.57079632679
2.0 -0.0
3.67708852834 0.491396861624
0.0 0.785398163397
12.7020515387 -0.092009761205
0.0 0.785398163397
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
125.895109131 0.613428963853
3.46410161514 0.785398163397
32.9740563066 1.54583302614
3.46410161514 -0.0
8.1929748235 0.459590902886
2.0 0.785398163397
10.5078026909 0.377072479866
13.7843641408 1.03885814981
3.70328039909 0.785398163397
6.44763580227 0.108130622936
38.8626242208 0.761942492676
52.9934087835 0.829988185861
6.84375679928 1.06683227982
6.14630682799 0.840294621974
4.46409815432 0.819436392526
7.2506157374 -1.57079632679
3.70328039909 -0.785398163397
15.297715489 1.47721210021
10.7594488352 1.23009407757
13.9302838351 0.866862678061
262.819664851 -0.667475162005
24.8416675082 0.668029191807
3.46410161514 -1.57079632679
31.4368697403 0.102624979119
8.11602466285 -0.241723500784
87.0048390772 0.917919701729
3.46410161514 -0.0
farzuntu python cell_migration.py
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:106: UserWarning: Possible sign loss when converting negative image of type float64 to positive image of type bool.
  "%s to positive image of type %s." % (dtypeobj_in, dtypeobj))
/home/farzuntu/.local/lib/python2.7/site-packages/skimage/util/dtype.py:110: UserWarning: Possible precision loss when converting from float64 to bool
  "%s to %s" % (dtypeobj_in, dtypeobj))
155.41413983 0.61182400465
3.46410161514 -1.57079632679
73.6821521535 1.17230335915
133.063229519 0.656614798136
7.05816530493 1.49379886641
3.46410161514 -0.0
20.0115217307 0.907572110075
63.5067220329 1.45797980015
3.46410161514 0.785398163397
251.749246382 -0.563278465522
19.5295180644 -0.416083895729
4.73286382648 -0.0
7.82504337486 -0.986268528854
farzuntu 