import numpy as np
from matplotlib.axes import Axes


def shareaxes(
    axes: np.ndarray, *,
    sharex=False, sharey=False,
    keepxlabels=False, keepylabels=False,
    vertical=False
):
    """Share X/Y axes of two or more `Axes` after they have been created.

    Parameters
    ----------
    axes: 1-d or 2-d array of `Axes`
        An array of `Axes` whose X/Y axes will be shared.
    sharex: bool
        Set `True` to share X axis.
    sharey: bool
        Set `True` to share Y axis.
    keepxlabels: bool
        Set `True` to keep X labels.
    keepylabels: bool
        Set `True` to keep Y labels.
    vertical: bool, optional
        `shareaxes([ax1, ax2], ..., vertical=True)` is equivalent to
        `shareaxes(np.atleast_2d([ax1, ax2]).T, ..., vertical=False)`.
        When 1-d array of `Axes` is passed, it will be assumed to be arranged 
        horizontally by default. If `vertical` is set to `True`, axes are
        assumed to be arranged vertically.

    Returns
    -------
    None
    """
    axes = np.atleast_2d(axes)
    if vertical:
        axes = axes.transpose()
    a0: Axes = axes[0, 0]
    ny, nx = np.shape(axes)
    for iy in range(ny):
        for ix in range(nx):
            a: Axes = axes[iy, ix]
            if iy != 0 or ix != 0:
                if sharex:
                    a0.get_shared_x_axes().join(a0, a)
                if sharey:
                    a0.get_shared_y_axes().join(a0, a)
            if sharex and iy != ny - 1 and not keepxlabels:
                a.set_xticklabels([])
                a.set_xlabel("")
            if sharey and ix != 0 and not keepylabels:
                a.set_yticklabels([])
                a.set_ylabel("")
