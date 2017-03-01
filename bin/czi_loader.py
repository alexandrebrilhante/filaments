# load tiff file here
from PIL import Image
import czifile
import numpy as np
from scipy import stats
#from skimage import restoration
import matplotlib.pyplot as plt

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
    return z_slice_size, chann1_im_list, chann2_im_list


if __name__ == '__main__':
    array = load_czi_file_as_stack('../data/original file.czi')
    z_slice_size, chann1_im_list, chann2_im_list = get_the_two_channel(array)
    # example by plotting
    N_rows = 2
    N_cols = 3
    fig, ax_grid = plt.subplots(N_rows, N_cols)
    for col in range(N_cols):
        im1_chan1 = chann1_im_list.pop()
        im1_chan2 = chann2_im_list.pop()
        ax_grid[0][col].imshow(im1_chan1)
        ax_grid[1][col].imshow(im1_chan2)
    plt.show()
