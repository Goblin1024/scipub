"""
Journal style configuration — set publication-quality Matplotlib defaults.

Provides column-width presets for major journals and convenience functions
for creating and saving figures at the correct dimensions.
"""

import os
import matplotlib as mpl
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────────────────────
# Journal column widths (inches)
# ──────────────────────────────────────────────────────────────────────
COLUMN_WIDTHS = {
    "nature":   {"single": 3.25, "double": 6.69, "max": 7.48},
    "science":  {"single": 3.35, "double": 6.85, "max": 7.20},
    "cell":     {"single": 3.35, "double": 6.85, "max": 7.20},
    "prl":      {"single": 3.37, "double": 6.69, "max": 6.69},
    "ieee":     {"single": 3.50, "double": 7.16, "max": 7.50},
    "jcp":      {"single": 3.33, "double": 6.67, "max": 6.67},
}

ASPECT_RATIOS = {
    "square": 1.0,
    "golden": 1.618,
    "wide":   1.5,
    "tall":   0.75,
    "half":   0.5,
    "hd":     1.778,
}


# ──────────────────────────────────────────────────────────────────────
# Style
# ──────────────────────────────────────────────────────────────────────

def set_style(journal="nature", latex=False):
    """Apply a top-journal Matplotlib style.

    Parameters
    ----------
    journal : str
        One of ``"nature"``, ``"science"``, ``"ieee"``, ``"aps"``,
        ``"scatter"``, ``"notebook"``.
    latex : bool
        Use LaTeX for text rendering (requires a working LaTeX installation).
    """
    # Try scienceplots first
    try:
        import scienceplots  # noqa: F401

        plt.style.use(["science", journal])
        mpl.rcParams["text.usetex"] = False  # don't require LaTeX
    except ImportError:
        _manual_rcparams()

    if latex:
        try:
            mpl.rcParams.update({
                "text.usetex": True,
                "text.latex.preamble": r"\usepackage{amsmath}",
                "font.family": "serif",
                "font.serif": ["Times", "Times New Roman"],
            })
        except Exception:
            print("Warning: LaTeX unavailable, falling back to sans-serif")
            mpl.rcParams.update({
                "font.family": "sans-serif",
                "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
            })
    else:
        mpl.rcParams.update({
            "font.family": "sans-serif",
            "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        })

    # Common publication refinements
    mpl.rcParams.update({
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.minor.width": 0.4,
        "ytick.minor.width": 0.4,
        "xtick.major.size": 3.5,
        "ytick.major.size": 3.5,
        "xtick.minor.size": 2.0,
        "ytick.minor.size": 2.0,
        "lines.linewidth": 1.2,
        "lines.markersize": 4,
        "legend.frameon": False,
        "legend.handlelength": 1.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def _manual_rcparams():
    """Fallback when scienceplots is not installed."""
    mpl.rcParams.update({
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "font.size": 8,
        "axes.labelsize": 8,
        "axes.titlesize": 9,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.2,
        "lines.markersize": 4,
        "legend.frameon": False,
    })


# ──────────────────────────────────────────────────────────────────────
# Figure creation
# ──────────────────────────────────────────────────────────────────────

def make_fig(journal="nature", columns=1, aspect="golden",
             nrows=1, ncols=1, figsize=None):
    """Create a figure with journal-appropriate dimensions.

    Parameters
    ----------
    journal : str
        Journal name (see ``COLUMN_WIDTHS``).
    columns : int
        1 = single-column, 2 = double-column.
    aspect : str | float
        ``"golden"``, ``"square"``, ``"wide"``, or a numeric ratio.
    nrows, ncols : int
        Subplot grid.
    figsize : tuple | None
        Override automatic sizing.

    Returns
    -------
    fig : matplotlib.figure.Figure
    axs : Axes or array of Axes
    """
    if figsize is not None:
        return plt.subplots(nrows, ncols, figsize=figsize)

    width = COLUMN_WIDTHS.get(journal, COLUMN_WIDTHS["nature"])[
        "single" if columns == 1 else "double"
    ]
    ratio = ASPECT_RATIOS.get(aspect, aspect) if isinstance(aspect, str) else aspect
    height = width / ratio

    return plt.subplots(nrows, ncols, figsize=(width, height * max(nrows, 1)))


def savefig(fig, basename, output_dir="figures", formats=("pdf", "png"),
            dpi=300, close=True):
    """Save a figure in one or more formats.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
    basename : str
        File name (with or without directory prefix).
    output_dir : str
        Output directory (created automatically).
    formats : tuple of str
        ``"pdf"``, ``"png"``, ``"eps"``, ``"svg"``.
    dpi : int
        Resolution for raster formats.
    close : bool
        Close the figure after saving to free memory.
    """
    if "/" in basename:
        output_dir = os.path.dirname(basename)
        basename = os.path.basename(basename)
    os.makedirs(output_dir, exist_ok=True)

    for fmt in formats:
        path = os.path.join(output_dir, f"{basename}.{fmt}")
        fig.savefig(path, dpi=dpi, bbox_inches="tight", pad_inches=0.02)
        print(f"  [{fmt.upper()}] {path}")

    if close:
        plt.close(fig)


# ──────────────────────────────────────────────────────────────────────
# Axes helpers
# ──────────────────────────────────────────────────────────────────────

def polish_axes(ax, spine_style="default", grid=False):
    """Refine axes appearance to journal standards.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
    spine_style : str
        ``"default"`` — bottom/left spines only (Nature style),
        ``"box"`` — all spines, ``"none"`` — no spines.
    grid : bool
        Show a light grid.
    """
    if spine_style in ("default", "bottom-left"):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(top=False, right=False)
    elif spine_style == "none":
        for s in ax.spines.values():
            s.set_visible(False)

    ax.tick_params(direction="in")
    if grid:
        ax.grid(True, linestyle=":", alpha=0.4, linewidth=0.4)


def colorbar_label(cbar, label, fontsize=7):
    """Add a styled label to a colorbar.

    Parameters
    ----------
    cbar : matplotlib.colorbar.Colorbar
    label : str
    fontsize : int
    """
    cbar.set_label(label, fontsize=fontsize)
    cbar.ax.tick_params(labelsize=6)
    return cbar
