#!/usr/bin/env python3
"""
04_multi_panel.py — Multi-panel figure with field comparison + error map.

Usage:
    python examples/04_multi_panel.py
"""

import sys
sys.path.insert(0, 'src')

import numpy as np
import matplotlib.pyplot as plt
import scipub

scipub.set_style('nature')
fig, axs = scipub.make_fig('nature', columns=2, aspect=0.8, nrows=1, ncols=3)

X, Y = np.meshgrid(np.linspace(-3, 3, 80), np.linspace(-3, 3, 80))
exact = np.exp(-(X**2 + Y**2)) * np.sin(2*X) * np.cos(2*Y)
predicted = exact * 0.92 + 0.08 * np.sin(3*X) * np.cos(3*Y)

cm = scipub.get_cmap('batlow')
vmin, vmax = exact.min(), exact.max()

for ax, data, title in zip(axs, [exact, predicted, exact - predicted],
                            ['Exact', 'Predicted', 'Difference']):
    c = ax.contourf(X, Y, data, levels=30, cmap=cm, vmin=vmin, vmax=vmax)
    ax.set_title(title, fontsize=8)
    ax.set_xlabel('r')
    ax.set_ylabel('z')
    scipub.polish_axes(ax)
    fig.colorbar(c, ax=ax, shrink=0.7)

fig.tight_layout()
scipub.savefig(fig, '04_multi_panel', output_dir='figures')
print("Done — see figures/04_multi_panel.pdf / .png")
