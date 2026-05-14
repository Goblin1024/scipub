"""
Perceptually uniform scientific colour maps.

Wraps CMasher, Fabio Crameri's Scientific Colour Maps (cmcrameri),
and Matplotlib defaults in a single ``get_cmap()`` interface.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

# Maps that exist in cmcrameri but not in CMasher
CRAMERI_MAPS = {
    "batlow", "batlowK", "batlowW", "berlin", "bilbao",
    "broc", "brocO", "buda", "cork", "corkO", "davos",
    "devon", "grayC", "hawaii", "imola", "lajolla",
    "lapaz", "lisbon", "nuuk", "oleron", "oslo",
    "roma", "romaO", "tofino", "tokyo", "turku",
    "vik", "vikO",
}


def get_cmap(name="batlow"):
    """Return a perceptually uniform scientific colour map.

    Resolution order:

    1. **CMasher** — ``amber``, ``fall``, ``freeze``, ``guppy``,
       ``lilac``, ``cosmic``, …, 50+ sequential/diverging maps.
    2. **Crameri** (cmcrameri) — ``batlow``, ``vik``, ``berlin``,
       ``roma``, ``tokyo``, ``hawaii``, …
    3. **Matplotlib** fallback — ``viridis``.

    Parameters
    ----------
    name : str
        Colour map name.

    Returns
    -------
    cmap : matplotlib.colors.Colormap
    """
    # 1. CMasher
    try:
        import cmasher as cmr  # noqa: F401

        if hasattr(cmr, name):
            return getattr(cmr, name)
    except ImportError:
        pass

    # 2. Crameri (cmcrameri registers as "cmr.*" in plt.colormaps)
    try:
        import cmcrameri  # noqa: F401 — registers the colormaps
    except ImportError:
        pass

    try:
        return plt.get_cmap(f"cmr.{name}")
    except ValueError:
        pass

    # 3. matplotlib default
    try:
        return plt.get_cmap(name)
    except ValueError:
        return plt.get_cmap("viridis")


def cycle_colors(n, cmap="batlow"):
    """Generate *n* evenly-spaced colours from a scientific colour map.

    Parameters
    ----------
    n : int
        Number of colours.
    cmap : str
        Colour map name (see :func:`get_cmap`).

    Returns
    -------
    list of RGBA tuples
    """
    cmap_obj = get_cmap(cmap)
    if cmap_obj is None:
        return [plt.get_cmap("viridis")(i / (n - 1)) for i in range(n)]
    return [cmap_obj(i / (n - 1)) for i in range(n)]


def set_default_cmap(name="batlow"):
    """Set the default image colour map globally.

    Parameters
    ----------
    name : str
        Colour map name.
    """
    cmap = get_cmap(name)
    if cmap is not None:
        mpl.rcParams["image.cmap"] = name
