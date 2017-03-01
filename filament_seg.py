# load tiff file here
from PIL import Image
from czifile import CziFile
import numpy as np

def load_tiff_as_array(filename):
    im = Image.open(filename)
    return np.asarray(im)

# import czi file
def load_czi_file_as_stack(filename):
    with CziFile(filename) as czi:
        image_arrays = czi.asarray()
    return image_arrays

if __name__ == '__main__':
    array = load_czi_file_as_stack('original file.czi')
    print(array.shape)

    import matplotlib.pyplot as plt

    # This indexing gives us full sized images in region 1
    # Some playing was required to extract the correct data.
    images = [array[0,0,0,index].T[0] for index in range(18)]

    # To fit on the screen in a nice way, we can arange the 
    # z-stack in a grid of 6x3 on a large figure.
    N_rows = 6
    N_cols = 3
    fig, ax_grid = plt.subplots(N_rows, N_cols, figsize=(N_cols*10,N_rows*10))

    for row in range(N_rows):
        for col in range(N_cols):
            image = images.pop()
            ax_grid[row][col].imshow(image)
    plt.show()