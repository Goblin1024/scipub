#!/usr/bin/env python3
"""
01_basic_line_plot.py — Line curves with Nature journal style.

Usage:
    python examples/01_basic_line_plot.py
"""

import sys
sys.path.insert(0, 'src')

import numpy as np
import scipub

scipub.set_style('nature')
fig, ax = scipub.make_fig('nature', columns=1, aspect='golden')

x = np.linspace(0, 2*np.pi, 100)
colors = scipub.cycle_colors(3, 'batlow')

ax.plot(x, np.sin(x), color=colors[0], label=r'$\sin(x)$')
ax.plot(x, np.cos(x), color=colors[1], linestyle='--', label=r'$\cos(x)$')
ax.plot(x, np.sin(x)*np.cos(x), color=colors[2], linestyle=':',
        label=r'$\sin(x)\cos(x)$')

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.legend()
scipub.polish_axes(ax)

scipub.savefig(fig, '01_line_curves', output_dir='figures')
print("Done — see figures/01_line_curves.pdf / .png")
