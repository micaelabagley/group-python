# Playing with Plotting

(**The info in this README is also available, and probably more readable, in the playing_with_plotting.ipynb**)

What follows includes some exercises/challenges related to plotting and displaying data in Python. 

The goal is to provide an opportunity to play with different types of data and explore ways of displaying it. You don't need to do every single exercise, and you don't need to do them all today. Hopefully this can serve as a useful reference for future work. 

There are multiple ways to do each of these, and everyone has their favorite. There are no 'right' answers.

The exercies that follow relate to:  
- [1D spectra](#1dspectra)
- [Scatter plots](#scatter)
- [Images](#image)
- [Random Tricks](#tricks)

---

<a id='1dspectra'></a>
## 1D spectra

In this directory is a 1d spectrum from SDSS of a z~0.076 star-forming galaxy.  
The same spectrum is available in two file formats: `spec.dat` and `spec.fits`  

The wavelength is in units of $A$ and the flux and flux error are in units of $10^{-17}$ erg/s/cm$^2$/$A$

**Read in the spectrum**  
Options include `numpy.genfromtxt`, `astropy.table.Table`, `astropy.io.fits`

**Plot the spectrum including errors**

**Measure emission line fluxes**  

In this spectrum, there is an H$\alpha$ emission line at 6563 $A$ $\times$ $(1+z)$. What is the flux of this line?

Consider trying:
- directly integrating the flux of the line (you might explore one of the modules in `scipy.integrate`)
- fitting a Gaussian to the line (maybe `scipy.optimize.curve_fit`)

and comparing the fluxes you get with either method

**Bonus: try fitting other profiles to the line, such as a Lorentzian or Voight profile**


---
<a id='scatter'></a>
## Scatter plots

In this directory there is another file `galSpecSubset-dr8.fits` containing some measurements from spectra for a subset of the [MPA-JHU value-added SDSS catalog](https://www.sdss.org/dr12/spectro/galaxy_mpajhu/). These measurements were released for SDSS data release 8 and are named after the Max Planck Institute for Astrophysics and the Johns Hopkins University where the measurement technique was developed (see [Brinchmann et al. 2004](http://adsabs.harvard.edu/abs/2004MNRAS.351.1151B), [Kauffmann et al. 2003](http://adsabs.harvard.edu/abs/2003MNRAS.341...33K), and [Tremonti et al. 2004](http://adsabs.harvard.edu/abs/2004ApJ...613..898T)).

The subset of data here includes
- `logmass`: log$_{10}$(mass [$M_{\odot}$]),
- `logsfr`: log$_{10}$(star formation rate [$M_{\odot}$/yr]), and 
- `haflux`: H$\alpha$ line flux in units of $10^{-17}$ erg/s/cm$^2$/$A$ 

for ~0.3% of the full catalog. 


**Create a scatter plot showing `logmass` vs `logsfr`. Color-code your points by `haflux`**

**Use a logarithmic color scaling (and colorbar) for the `haflux` values**

**Plot a histogram of `haflux` values**

**Plot `logmass` vs `logsfr` as a 2D histogram**

**Plot `logmass` vs `logsfr` vs `haflux` as a 3D scatter plot**

_Hint:_   
`from mpl_toolkits.mplot3d import Axes3D`  
`fig = plt.figure()`  
`ax = fig.add_subplot(111, projection='3d')`


**Find all points that lie in a specific region**

There is a table of random x and y values called `random_scatter.fits`.

- How many/which points are within a circle centered at (0,0.4) with a radius of 0.2?
- How many/which points are within a square centered at the same point with side length 0.2?
- How many/which points are within the polygon defined by the corners: [-1.3,0.8], [0.7,0.6], [0.4,0.3], [-1,0.5]? 


---
<a id='image'></a>
## 2D Images

There are 5 images in fits format: `image1.fits`, etc. Each one contains an image of a source with some cool structure. The full extent of the structure will not be visible until you find an optimal stretch and scaling for displaying the image. 

Pick an image at random or play with all of them! `image5.fits` is a particular challenge because of nearby bright sources/artifacts in the image. 


**Display the image**

If you're using `matplotlib`:  
`plt.imshow(...)`  
And remember that you need the keyword `origin='lower'` to place the [0,0] index of the array in the lower left corner like our brains usually want.


**Change color maps, play with changing the vmin,vmax scaling**


**`astropy.visualization` includes some very useful functions for optimal stretching/scaling of image data**


**Bonus: display a ds9 region on top of the image**

There's a ds9 regions file (`ds9.reg`) with two regions: a green square and a blue circle.    
Use `pyregion` to display both regions on top of the image.


**Bonus: display the image with WCS coordinates/axes**

_Hint:_  
`astropy.wcs.WCS` will get all the WCS information (RA,Dec, etc.) from the header. You can create a subplot with a `wcs` projection (similar to the `3d` projection above, but with the WCS defined in the image header)


---
<a id='tricks'></a>
## Random Tricks

An assortment of random tricks

**Defining a figure**  
Defining an instance of a Figure object gives you more control over plotting options than making all plotting commands with `plt`. 

You can define a figure:  
`fig = plt.figure()`  
Then add an axis:  
`ax = fig.add_subplot(111)`  
And to plot to the axis:  
`ax.plot(...)`

You can create a figure and grid of axes all in one go:  
`fig,(ax1,ax2) = plt.subplots(1, 2)`

Setting `tight_layout` will make pyplot optimize the placement of all your axes automatically:  
`fig,(ax1,ax2) = plt.subplots(1, 2, tight_layout=True)`  
or:  
`plt.tight_layout()`

Defining a figure lets you save it to disk:  
`fig.savefig('figure.png')`  
`fig.savefig('figure.pdf')`


**Iterate through plotting symbols**  
In a similar way you can iterate through markers when making a scatter plot (or a line plot with markers):

```
import itertools
marker = itertools.cycle(('s', '+', '.', 'o', '*')) 
for thing in things_to_plot:
    plt.scatter(x, y, marker=next(marker))
```


**Create your own plot symbol**  
For example, to create an upper limit arrow:  

```
import numpy as np
from matplotlib.path import Path


def upper_limit():
    """Create a marker for an upper limit - empty box with arrow"""
    verts = [(0,2),(2,2),(2,-2),(-2,-2),(-2,2),(0,2),
             (0,7.5),(2.5,5.5),(0,7.5),(-2.5,5.5),(0,7.5),(0,2)]
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
             Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO,
             Path.LINETO, Path.LINETO]
    path = Path(verts, codes)
    return path
    
plt.scatter(x, y, marker=upper_limit(), s=800)
plt.plot(x, y, marker=upper_limit(), ms=30)
```
(You have to scale up the size of the symbol)


**Use an image as a plot symbol**  
Can we make a scatter plot of JWST mirrors? Why, yes we can!  

```
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

xx = [0,1,2,3,4]
yy = [0,1,2,3,4]

fig, ax = plt.subplots()
ax.plot(xx, yy)
# read in the image
image = plt.imread('mirror.png')
# we have to scale down the image size (or use a different coordiate system for display)
im = OffsetImage(image, zoom=0.05)
for x,y in zip(xx,yy):
    ab = AnnotationBbox(im, (x, y), frameon=False)
    ax.add_artist(ab)
```
