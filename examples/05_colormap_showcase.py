#!/usr/bin/env python3
"""
05_colormap_showcase.py — Show all available colormap families.

Usage:
    python examples/05_colormap_showcase.py
"""

import sys
sys.path.insert(0, 'src')

import numpy as np
import matplotlib.pyplot as plt
import scipub

scipub.set_style('nature')

# Check what's available
available = {'cmasher': [], 'crameri': [], 'matplotlib': []}

try:
    import cmasher as cmr
    available['cmasher'] = ['amber', 'fall', 'freeze', 'guppy', 'lilac',
                            'cosmic', 'arctic', 'bubblegum']
except ImportError:
    pass

try:
    import cmcrameri  # noqa: F401
    available['crameri'] = ['batlow', 'vik', 'berlin', 'roma', 'tokyo',
                            'hawaii', 'oslo', 'turku', 'imola', 'devon']
except ImportError:
    pass

available['matplotlib'] = ['viridis', 'plasma', 'inferno', 'magma']

# Create gradient data
gradient = np.linspace(0, 1, 256).reshape(1, -1)

n_maps = sum(len(v) for v in available.values())
fig, axs = plt.subplots(n_maps, 1, figsize=(6, 0.35 * n_maps))
fig.subplots_adjust(hspace=0.4)

row = 0
for family, maps in available.items():
    for name in maps:
        ax = axs[row]
        cmap = scipub.get_cmap(name)
        ax.imshow(gradient, aspect='auto', cmap=cmap)
        ax.set_ylabel(name, fontsize=7, rotation=0, ha='right', va='center')
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
        row += 1

axs[0].set_title('scipub colormap gallery', fontsize=9, fontweight='bold')
fig.savefig('figures/05_colormaps.pdf', bbox_inches='tight')
fig.savefig('figures/05_colormaps.png', bbox_inches='tight', dpi=200)
plt.close(fig)
print("Done — see figures/05_colormaps.pdf / .png")
