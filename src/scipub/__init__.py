"""
scipub — Publication-Quality Scientific Figures, One Line Away.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lightweight Matplotlib toolkit for generating Nature/Science/Cell/PRL/IEEE
level figures from scientific data. Built on SciencePlots + CMasher + Crameri
colormaps with zero configuration required.

Basic usage::

    >>> import scipub
    >>> scipub.set_style('nature')
    >>> fig, ax = scipub.make_fig()
    >>> ax.plot(x, y)
    >>> scipub.savefig(fig, 'my_figure')

See README.md and the examples/ directory for more.
"""

__version__ = "0.1.0"
__author__ = "spirit"

from scipub.journal import (
    set_style,
    make_fig,
    savefig,
    polish_axes,
    colorbar_label,
    COLUMN_WIDTHS,
    ASPECT_RATIOS,
)
from scipub.colormaps import (
    get_cmap,
    cycle_colors,
    set_default_cmap,
    CRAMERI_MAPS,
)
from scipub.templates import (
    plot_curves,
    plot_field,
    plot_field_comparison,
    plot_error_map,
    plot_training_curves,
    demo,
)
