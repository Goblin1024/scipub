"""
Convenience plot templates for common scientific visualisation tasks.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from scipub.journal import set_style, make_fig, savefig, polish_axes, colorbar_label
from scipub.colormaps import get_cmap, cycle_colors


def plot_curves(x, y_dict, xlabel="x", ylabel="y", title=None,
                save_to=None, journal="nature"):
    """Plot one or more 1-D curves with journal styling.

    Parameters
    ----------
    x : array-like
    y_dict : dict of str → array-like
        ``{label: y_values}`` pairs.
    xlabel, ylabel : str
    title : str | None
    save_to : str | None
        If set, save figure to this path (without extension).
    journal : str

    Returns
    -------
    fig, ax
    """
    set_style(journal)
    fig, ax = make_fig(journal, columns=1, aspect=1.4)
    colors = cycle_colors(len(y_dict), "batlow")

    for (label, y), c in zip(y_dict.items(), colors):
        ax.plot(x, y, color=c, label=label)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    polish_axes(ax)

    if title:
        ax.set_title(title, fontsize=9)

    if save_to:
        savefig(fig, save_to)
    return fig, ax


def plot_field(r_grid, z_grid, field, xlabel="r", ylabel="z",
               cbar_label="", cmap="batlow", title=None,
               save_to=None, journal="nature"):
    """Plot a 2-D field as a filled contour map.

    Parameters
    ----------
    r_grid, z_grid : 2-D array
        Meshgrid coordinates.
    field : 2-D array
        Scalar field to visualise.
    xlabel, ylabel : str
    cbar_label : str
        Colour bar label.
    cmap : str
        Colour map name.
    title : str | None
    save_to : str | None
    journal : str

    Returns
    -------
    fig, ax
    """
    set_style(journal)
    fig, ax = make_fig(journal, columns=1, aspect=1.0)

    cm = get_cmap(cmap)
    c = ax.contourf(r_grid, z_grid, field, levels=30, cmap=cm)
    cb = fig.colorbar(c, ax=ax, shrink=0.8)
    colorbar_label(cb, cbar_label)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    polish_axes(ax)

    if title:
        ax.set_title(title, fontsize=9)

    if save_to:
        savefig(fig, save_to)
    return fig, ax


def plot_field_comparison(r_grid, z_grid, exact, predicted,
                          save_to=None, title=None, journal="nature"):
    """Side-by-side comparison of exact and predicted 2-D fields.

    Parameters
    ----------
    r_grid, z_grid : 2-D array
    exact, predicted : 2-D array
    save_to : str | None
    title : str | None
    journal : str

    Returns
    -------
    fig, (ax_left, ax_right)
    """
    set_style(journal)
    fig, axs = make_fig(journal, columns=2, aspect=0.6, nrows=1, ncols=2)

    cm = get_cmap("batlow")
    vmin = min(exact.min(), predicted.min())
    vmax = max(exact.max(), predicted.max())

    for ax, data, label in zip(axs, [exact, predicted],
                                ["Exact", "Predicted"]):
        c = ax.contourf(r_grid, z_grid, data, levels=30, cmap=cm,
                        vmin=vmin, vmax=vmax)
        ax.set_xlabel("r")
        ax.set_ylabel("z")
        ax.set_title(label, fontsize=8)
        polish_axes(ax)
        fig.colorbar(c, ax=ax, shrink=0.8)

    if title:
        fig.suptitle(title, fontsize=9, y=1.02)

    fig.tight_layout()
    if save_to:
        savefig(fig, save_to)
    return fig, axs


def plot_error_map(r_grid, z_grid, exact, predicted,
                   save_to=None, journal="nature"):
    """Relative error map between exact and predicted fields.

    Uses a diverging colour map (``vik``) to highlight positive and
    negative deviations.

    Returns
    -------
    fig, ax
    """
    set_style(journal)
    fig, ax = make_fig(journal, columns=1, aspect=1.0)

    rel_err = np.abs((exact - predicted)
                     / (np.maximum(np.abs(exact), 1e-10)))
    cm = get_cmap("vik")
    c = ax.contourf(r_grid, z_grid, rel_err, levels=30, cmap=cm)
    cb = fig.colorbar(c, ax=ax, shrink=0.8)
    colorbar_label(cb, "Relative Error")

    ax.set_xlabel("r")
    ax.set_ylabel("z")
    polish_axes(ax)

    if save_to:
        savefig(fig, save_to)
    return fig, ax


def plot_training_curves(history, save_to=None, journal="nature"):
    """Plot training / validation loss curves.

    Parameters
    ----------
    history : dict
        With keys ``"train_loss"`` and optionally ``"val_loss"``.
    save_to : str | None
    journal : str

    Returns
    -------
    fig, ax
    """
    set_style(journal)
    fig, ax = make_fig(journal, columns=1, aspect=1.4)

    colors = cycle_colors(2, "batlow")
    epochs = range(1, len(history["train_loss"]) + 1)

    ax.plot(epochs, history["train_loss"], color=colors[0], label="Train")
    if "val_loss" in history:
        ax.plot(epochs, history["val_loss"], color=colors[1],
                label="Validation", linestyle="--")

    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.set_yscale("log")
    ax.legend()
    polish_axes(ax)

    if save_to:
        savefig(fig, save_to)
    return fig, ax


# ──────────────────────────────────────────────────────────────────────
# Demo
# ──────────────────────────────────────────────────────────────────────

def demo(output_dir="figures"):
    """Run a full demonstration, generating all example figures.

    Parameters
    ----------
    output_dir : str
        Directory where figures are saved.
    """
    print("=" * 50)
    print("scipub demo — generating example figures")
    print("=" * 50)

    # Verify key dependencies
    for pkg in ["scienceplots", "matplotlib"]:
        try:
            __import__(pkg)
            print(f"  ✓ {pkg}")
        except ImportError:
            print(f"  ✗ {pkg} — install with: pip install {pkg}")

    print()

    # ── 1. Line curves ──────────────────────────────────────────────
    print("[1/4] Line curves …")
    x = np.linspace(0, 2 * np.pi, 100)
    fig, ax = plot_curves(
        x,
        {
            r"$\sin(x)$": np.sin(x),
            r"$\cos(x)$": np.cos(x),
            r"$\sin(x)\cos(x)$": np.sin(x) * np.cos(x),
        },
        xlabel="$x$",
        ylabel="$y$",
        save_to=os.path.join(output_dir, "01_line_curves"),
    )
    print(f"  ✓  {os.path.join(output_dir, '01_line_curves.*')}")

    # ── 2. 2-D field ────────────────────────────────────────────────
    print("[2/4] 2-D field …")
    X, Y = np.meshgrid(np.linspace(-3, 3, 80), np.linspace(-3, 3, 80))
    Z = np.exp(-(X**2 + Y**2)) * np.sin(2 * X) * np.cos(2 * Y)
    fig, ax = plot_field(
        X, Y, Z,
        xlabel="$r$", ylabel="$z$",
        cbar_label="Temperature",
        save_to=os.path.join(output_dir, "02_2d_field"),
    )
    print(f"  ✓  {os.path.join(output_dir, '02_2d_field.*')}")

    # ── 3. Field comparison ─────────────────────────────────────────
    print("[3/4] Field comparison …")
    fig, axs = plot_field_comparison(
        X, Y, Z, Z * 0.95,
        title="Neural Operator: Exact vs Predicted",
        save_to=os.path.join(output_dir, "03_field_comparison"),
    )
    print(f"  ✓  {os.path.join(output_dir, '03_field_comparison.*')}")

    # ── 4. Training curves ──────────────────────────────────────────
    print("[4/4] Training curves …")
    rng = np.random.default_rng(42)
    history = {
        "train_loss": np.exp(-np.linspace(0, 3, 50))
                      + 0.01 * rng.standard_normal(50).cumsum(),
        "val_loss": np.exp(-np.linspace(0, 2.5, 50))
                    + 0.02 * rng.standard_normal(50).cumsum(),
    }
    fig, ax = plot_training_curves(
        history,
        save_to=os.path.join(output_dir, "04_training_curves"),
    )
    print(f"  ✓  {os.path.join(output_dir, '04_training_curves.*')}")

    print()
    print(f"✓ All figures saved to '{output_dir}/'")
    print("=" * 50)
    return output_dir
