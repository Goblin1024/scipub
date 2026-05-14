# scipub — Agent Instructions

This file tells AI coding agents (Claude Code, OpenCode, Cursor, Copilot, etc.)
how to use scipub correctly. The package itself is pure Python with zero
external agent dependency.

## One-sentence summary

`scipub` is a **pip-installable Python library** that makes Matplotlib produce
Nature/Science/Cell/PRL/IEEE-level figures in one line of code.

## Installation

```bash
# Minimal (Matplotlib + NumPy only)
pip install scipub

# Full (recommended — adds SciencePlots, CMasher, Crameri colormaps, Seaborn)
pip install "scipub[full]"

# From local source (development)
cd /path/to/scipub
pip install -e ".[full]"
```

## API — what to call when a user asks "make a plot"

### 1. Set journal style (call once at top of script)
```python
import scipub
scipub.set_style('nature')    # | or 'science' | 'ieee' | 'aps' | 'scatter'
```

### 2. Create a figure with correct dimensions
```python
fig, ax = scipub.make_fig('nature', columns=1, aspect='golden')
#                                 single | double     golden | square | wide
```

### 3. Use journal-grade colour maps
```python
# Get a colormap (auto-resolves CMasher → Crameri → Matplotlib)
cmap = scipub.get_cmap('batlow')   # Nature's favourite

# Generate colour cycle for line plots
colors = scipub.cycle_colors(5, 'batlow')

# Diverging map for error maps
cmap = scipub.get_cmap('vik')
```

### 4. Polish axes
```python
scipub.polish_axes(ax)                        # bottom-left spines (Nature style)
scipub.polish_axes(ax, spine_style='box')      # all spines
```

### 5. Save in multiple formats
```python
scipub.savefig(fig, 'output_name')            # → output_name.pdf + output_name.png
scipub.savefig(fig, 'output', formats=('svg', 'eps'))
```

### 6. Use built-in templates (quick plots)
```python
# 1-D curves
scipub.plot_curves(x, {"label1": y1, "label2": y2})

# 2-D field
scipub.plot_field(X, Y, Z, cbar_label='Temperature')

# Training curves
scipub.plot_training_curves({"train_loss": [...], "val_loss": [...]})

# Compare exact vs predicted
scipub.plot_field_comparison(X, Y, exact, predicted)

# Error map
scipub.plot_error_map(X, Y, exact, predicted)
```

### 7. Run demo
```python
from scipub import demo
demo()   # saves all example figures to figures/
```

## Common pitfalls

1. **Call `set_style()` before any plotting**, not after.
2. **Do not set `text.usetex = True`** unless LaTeX is actually installed.
   scipub disables it by default.
3. **Use `get_cmap('batlow')` for sequential**, `get_cmap('vik')` for
   diverging data. Avoid jet/rainbow.
4. **Figures look small on screen?** That's correct — Nature single column is
   3.25". The PDF will be the right size when inserted into the paper.
5. **Seaborn works alongside scipub**: just call `scipub.set_style('nature')`
   then `sns.set_theme(context='paper')`.

## Full example template

When a user asks you to "create a scientific plot" or "make this look
publication-quality," this is the standard pattern:

```python
import numpy as np
import scipub

# 1. Style
scipub.set_style('nature')

# 2. Figure
fig, ax = scipub.make_fig('nature', columns=1, aspect='golden')

# 3. Colours
colors = scipub.cycle_colors(N, 'batlow')

# 4. Data plotting
for i, (x, y) in enumerate(data_sets):
    ax.plot(x, y, color=colors[i], label=f'Label {i}')

# 5. Labels and legend
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# 6. Polish
scipub.polish_axes(ax)

# 7. Save
scipub.savefig(fig, 'output_name')
```

That's it — no Hermes, no environment-specific paths, no hidden dependencies.
