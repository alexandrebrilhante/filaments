# load tiff file here
from PIL import Image
import czifile
import numpy as np
from scipy import stats, ndimage
from skimage import restoration, exposure, morphology
from skimage.feature import canny, peak_local_max, match_template
import matplotlib.pyplot as plt
from skimage.filters import sobel, rank, gaussian
from skimage import segmentation, filters
#from skimage.morphology import thin


def load_tiff_as_array(filename):
    im = Image.open(filename)
    return np.asarray(im)

# import czi file
def load_czi_file_as_stack(filename):
    return czifile.imread(filename) 

def get_the_two_channel(array):
    # current shape
    # (1, 2, 1, 109, 1120, 1120, 1)
    # first position is not important
    # second is channel
    # third is not important
    # 4th is z-slice
    # 5 et 6th are im dimension
    # the last one is not important
    z_slice_size = array.shape[3]
    chann1_im_list = [array[0,0,0,index].T[0] for index in range(z_slice_size)]
    chann2_im_list = [array[0,1,0,index].T[0] for index in range(z_slice_size)]
    return z_slice_size, np.asarray(chann1_im_list, dtype=np.float32), np.asarray(chann2_im_list, dtype=np.float32)


def bilateral_denoise(chan):
    """magical stuff1"""
    return np.asarray([restoration.denoise_bilateral(x, multichannel=False) for x in chan])

def show_im(im):
    plt.imshow(im, cmap="gray")
    plt.show()

def scale_channel(chan):
    vmin, vmax = stats.scoreatpercentile(chan, (0.5, 99.5))
    dchan = (np.clip(chan, vmin, vmax) - vmin)/ (vmax-vmin)
    return dchan

def edge_compute(chan):
    edges = np.asarray([canny(im) for im in chan])
    return edges

def fill_holes_and_clean(edges):
    # fill holes for each slices
    filled_slices = [morphology.remove_small_objects(ndimage.binary_fill_holes(x)) for x in edges]
    return np.asarray(filled_slices)

def get_biggest_object_coverage(binary_ims):
    binary_z_projected = np.sum(binary_ims, axis=0)
    largest_blob = binary_z_projected > np.mean(binary_z_projected)
    return largest_blob
    

def sobel_on_each_slice(chan):
    return [sobel(x) for x in chan]

def fast_denoise(chan):
    denoised_chan = restoration.denoise_nl_means(chan, h=0.2, fast_mode=True)
    return denoised_chan

def compute_squeleton(binary_chan):
    skeleton = [morphology.skeletonize(im) for im in binary_chan]
    return skeleton

#def compute_thinner(binary_chan, max_iter=None):
#   thinned = [thin(im, max_iter) for im in binary_chan]
#   return thinned


if __name__ == '__main__':

    # desesperate algorithm_3 with stack slicing
    array = load_czi_file_as_stack('../data/original file.czi')
    _, chann1_im, chann2_im = get_the_two_channel(array)
    #rw, gchan = desesperate_algorithm1(chann1_im[10:2:100, 450:750, 450:750] , chann2_im[10:2:100, 450:750, 450:750])
    green_chan, red_chan = chann1_im[10:100, 450:750, 450:750] , chann2_im[10:100, 450:750, 450:750]
    scaled_green =  scale_channel(green_chan)
    scaled_red =  scale_channel(red_chan)
    bilats = bilateral_denoise(scaled_green)

    green_thresh = filters.threshold_otsu(bilats.max(axis=0))
    red_thresh = filters.threshold_otsu(scaled_red.max(axis=0))
    
    binary_bilats = bilats > green_thresh
    mask_fus = np.logical_and(binary_bilats>0, scaled_red>red_thresh)
    binary_bilats[np.logical_not(mask_fus)] = 0
    # let cleaned the binary before opening
    binary_bilats = fill_holes_and_clean(binary_bilats)
    # opening and closing using ball of size 4
    open_object = morphology.binary_opening(binary_bilats, morphology.ball(3))
    close_object = morphology.binary_closing(open_object, morphology.ball(3))
    # let's find all object in the morphological closed image
    # this represent the box enclosing the binary segmentation
    maxbox = ndimage.find_objects(close_object)
    # create a binary mask for enclosing the data
    bin_mask = np.asarray([ndimage.binary_fill_holes(x) for x in close_object[maxbox[0]]])
    # now restrict green chan to the bin mask

    # hoping here that 
    new_green_chan = scaled_green[maxbox[0]]
    g_fast_denoise = restoration.denoise_tv_chambolle(new_green_chan)
    max_project = np.max(new_green_chan, axis=0)
    
    #min_radius = 4
    #markers = []
    #smooth_size = 5
    #for z_ind in range(new_green_chan.shape[0]):
        #distance = ndimage.distance_transform_edt(bin_mask[z_ind])
        #smoothed = rank.median(new_green_chan[z_ind], morphology.disk(smooth_size))
        #smoothed = rank.enhance_contrast(smoothed, morphology.disk(smooth_size))        
        #local_maxi = peak_local_max(distance, min_distance=2*min_radius, indices=False, labels=smoothed)
        #markers.append(ndimage.label(local_maxi)[0])
    
    markers = np.zeros(g_fast_denoise.shape, dtype=np.uint8)
    markers[g_fast_denoise > 0.25] = 1
    markers[g_fast_denoise < 0.1] = 2
    rw = segmentation.random_walker(g_fast_denoise, np.asarray(markers), beta=500., mode='cg_mg')
    #rw = morphology.remove_small_objects(np.asarray(rw) == 1)
    squelton = compute_squeleton(bin_mask)
    blurreds = [ndimage.find_objects(gaussian(squelton[x], 3)>0)[0] for x in xrange(new_green_chan.shape[0])]
    smootheds = []
    for i in xrange(new_green_chan.shape[0]):
        smoothed = new_green_chan[i].copy()
        mask = np.zeros_like(smoothed)
        mask[blurreds[i]] = 1
        smoothed[np.logical_not(mask)] = 0
        smootheds.append(smoothed > np.mean(smoothed[blurreds[i]]))
    # taking 6 slices at regular interval
    fig, axs =  plt.subplots(2, 3)  
    start = 10
    for i, ax in enumerate(axs.reshape(-1)):
        ax.imshow(new_green_chan[start], cmap="gray")
        ax.contour(squelton[start], [0.5], linewidths=2)
        ax.contour(smootheds[start], color='k')
        ax.contour(rw[start], color="b")
        ax.set_title("z-slice "+str(start))
        start += (new_green_chan.shape[0] -11)/ 6 
    fig.savefig("test.png")

