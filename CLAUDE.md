# scipub — Publication-Quality Scientific Figures

A pip-installable Python library that makes Matplotlib produce Nature/Science/Cell
journal-level figures in one line of code.

## Quick start

```bash
pip install "scipub[full]"
```

```python
import scipub
scipub.set_style('nature')
fig, ax = scipub.make_fig()
ax.plot(x, y)
scipub.savefig(fig, 'output')
```

## Key design

- **Zero Hermes dependency** — pure Python, works anywhere
- **Agent-agnostic** — Claude Code, OpenCode, Cursor, Copilot all use it identically
- **Minimal API** — 7 public functions you can memorize in 30 seconds

For AI agent instructions, see `AGENTS.md`.
For full API, see `README.md`.

## Examples

```bash
python examples/01_basic_line_plot.py
python examples/02_2d_field.py
python examples/03_training_curves.py
python examples/generate_all.py
```
