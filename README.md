# Map Visualization Project

A Python project for creating and visualizing maps using Cartopy. This project provides tools for generating maps with administrative boundaries, including country borders and province/state boundaries.

## Features
- Create maps with customizable extents
- Display administrative boundaries
- Color-coded provinces/states
- Customizable map features (coastlines, borders, etc.)

## Requirements
- Python 3.x
- cartopy
- matplotlib
- numpy

## Installation
1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
4. Install requirements: `pip install cartopy matplotlib numpy`

## Usage
```python
from code.functions import plot_map_with_admin_boundaries

# Create a map with default settings
fig, ax = plot_map_with_admin_boundaries()

# Save the map
fig.savefig('exported_figs/map.png', dpi=300, bbox_inches='tight')
``` 