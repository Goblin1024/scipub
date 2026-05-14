#!/usr/bin/env python3
"""
generate_all.py — Regenerate all example figures.

Usage:
    python examples/generate_all.py
"""

import sys
sys.path.insert(0, 'src')

from scipub import demo

demo('figures')
