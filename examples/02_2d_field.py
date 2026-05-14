#!/usr/bin/env python3
"""
02_2d_field.py — 2-D field (contourf) with Crameri batlow colormap.

Usage:
    python examples/02_2d_field.py
"""

import sys
sys.path.insert(0, 'src')

import numpy as np
import scipub

scipub.set_style('nature')
fig, ax = scipub.make_fig('nature', columns=1, aspect=1.0)

X, Y = np.meshgrid(np.linspace(-3, 3, 80), np.linspace(-3, 3, 80))
Z = np.exp(-(X**2 + Y**2)) * np.sin(2*X) * np.cos(2*Y)

cm = scipub.get_cmap('batlow')
c = ax.contourf(X, Y, Z, levels=30, cmap=cm)
cbar = fig.colorbar(c, ax=ax, shrink=0.8)
scipub.colorbar_label(cbar, 'Temperature')

ax.set_xlabel(r'$r$')
ax.set_ylabel(r'$z$')
scipub.polish_axes(ax)

scipub.savefig(fig, '02_2d_field', output_dir='figures')
print("Done — see figures/02_2d_field.pdf / .png")
