# biohack2017

## Slides

[Google Slides](https://docs.google.com/presentation/d/17niwPZWo3tH1Cati9ne99XYlknP1iCIGK575ggo5obE/edit?usp=sharing)

## Data

Dans `data`:

+ `zscan3d-c2-crop-x700_800-y800_900.tsv.gz`: juste une partie de l'image 3D (sinon c'est trop gros). Les 4 colonnes sont: x, y, z et valeur. Les pixels noirs (valeur 0) ne sont pas présents pour gagner de l'espace. 

## Inspiration

+ [Passer d'un skeleton à un graph (en 2D)](https://gist.github.com/jeanpat/5712699): peut-être plus facile pour trouver les *bouts* et simplifier le calcul des summary stats.
+ [Segmentation of 3-D tomography images with Python and scikit-image](http://emmanuelle.github.io/segmentation-of-3-d-tomography-images-with-python-and-scikit-image.html)
+ [Trouver les points d'intérêts](http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_corner.html#sphx-glr-auto-examples-features-detection-plot-corner-py)