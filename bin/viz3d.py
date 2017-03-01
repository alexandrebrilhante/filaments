from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy


def plotSkel(skel):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax = fig.add_subplot(111, projection='3d')
    skxyz = numpy.where(skel > 0)
    surf = ax.scatter(skxyz[0], skxyz[1], skxyz[2])
    plt.show()


def plotSurf(skel):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    skxyz = numpy.where(skel > 0)
    surf = ax.plot_surface(skxyz[0], skxyz[1], skxyz[2])
    plt.show()


# sk = numpy.zeros((300, 300, 300), dtype=numpy.uint8)
# sk[2:280, 150, 150] = 1
# sk[150, 2:280, 150] = 1
# sk[200, 150, 3:200] = 1

# plotSkel(sk)

from skimage.draw import ellipsoid

img = ellipsoid(100, 100, 20)
img

plotSkel(img)
plotSurf(img)
