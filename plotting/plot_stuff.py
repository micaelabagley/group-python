import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def basic_figure():
    """create a basic figure and add a few subplots to it"""
    # define basic figure
    fig = plt.figure()
    # you can define a size in magic units
    fig = plt.figure(figsize=(10,6))

    # add an axis (or subplot)
    ax = fig.add_subplot(111)
    # the 111 means: (number of rows, number of columns, index of current plot)

    # so if you want to create a figure with 2 rows with 3 subplots per row:
    ax1 = fig.add_subplot(231)
    ax2 = fig.add_subplot(232)
    ax3 = fig.add_subplot(233)
    ax4 = fig.add_subplot(234)
    ax5 = fig.add_subplot(235)
    ax6 = fig.add_subplot(236)

    # use tight layout to optimize space
    plt.tight_layout() # only applies to the current working figure

    fig.savefig('basic_figure.pdf')


def subplots_figure():
    """create a figure and subplots all in one go
    the basic example only faster
    """
    # create a figure with one axis
    fig,ax = plt.subplots(1, 1, tight_layout=True)

    # a figure with 2 rows and 3 columns of equally-sized axes
    fig, ((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2, 3, tight_layout=True)

    # no need to apply tight_layout because it's already included
    fig.savefig('subplots_figure.png')  #saving this one as a png just cuz


def gridspec_figure():
    """gridspec gives you more control and lets you make multiple plots 
    of different sizes.

    gridspec is easiest to explain through an example
    """

    fig = plt.figure(figsize=(10,6))
    # define the shape and size of a grid that can take up any fraction 
    # of the figure
    gs = GridSpec(1,1)
    # GridSpec(nrows,ncols)

    # we next update where we want this grid to go, the numbers are 
    # figure units, specifying a position on the figure from 0 to 1
    gs.update(left=0.05, right=0.95, top=0.95, bottom=0.05)
    # now use this gridspec object to create a subplot
    ax = fig.add_subplot(gs[0])
    
    # new example: what if you want to make one subplot that spans the 
    # full figure on top, and two smaller subplots on the bottom?
    fig = plt.figure(figsize=(10,6))
    gs1 = GridSpec(1,1)
    gs1.update(left=0.05, right=0.95, top=0.95, bottom=0.55)
    ax1 = fig.add_subplot(gs1[0])
    gs2 = GridSpec(1,2)
    gs2.update(left=0.05, right=0.95, top=0.5, bottom=0.05)
    ax2 = fig.add_subplot(gs2[0,0])
    ax3 = fig.add_subplot(gs2[0,1])

    # tight_layout doesn't apply to gridspec because you've already
    # specified specifically where you want your subplots to go
    fig.savefig('gridspec_figure.pdf')


def inset_axis_things():
    # first define figure and axes however you want
    fig,ax = plt.subplots(1, 1, tight_layout=True)
    # now create the inset axis
    inset = ax.inset_axes([0.1,0.5,0.4,0.4])
    # [x of lower left corner, y of lower left corner, width, height]

    inset.plot(...)
    inset.set_xlim(...)
    inset.set_xlabel(...)

    # to get the box drawn on the full plot showing which region is 
    # zooming in:
    ax.indicate_inset_zoom(inset)


def histogram_things(data):
    """ """
    # make a histogram with bins determined by the freedman-diaconis rule
    hist,bin_edges = np.histogram(data, bins=fd)
    # define bin centers by taking the average of the bin edges
    bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])
    # now for curve plot you're fitting the distribution so:
    #  xvalues: bin_centers, yvalues: hist


