#!/usr/bin/env python3
"""
03_training_curves.py — Training/validation loss curves.

Usage:
    python examples/03_training_curves.py
"""

import sys
sys.path.insert(0, 'src')

import numpy as np
import scipub

rng = np.random.default_rng(42)
history = {
    'train_loss': np.exp(-np.linspace(0, 3, 50))
                  + 0.01 * rng.standard_normal(50).cumsum(),
    'val_loss':   np.exp(-np.linspace(0, 2.5, 50))
                  + 0.02 * rng.standard_normal(50).cumsum(),
}

scipub.plot_training_curves(history, save_to='figures/03_training_curves')
print("Done — see figures/03_training_curves.pdf / .png")
