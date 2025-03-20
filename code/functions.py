import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import warnings
import cartopy.io.shapereader as shpreader
import numpy as np
warnings.filterwarnings("ignore")


high_res_borders = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_0_boundary_lines_land',
    scale='10m',  # High resolution: '10m', medium: '50m', low: '110m'
    facecolor='none'
)

provinces = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_1_states_provinces_lines',
    scale='10m',
    facecolor='none'
)


def plot_map_with_admin_boundaries(figsize=(8, 8), extent=[-75, -55, -57, -32]):
    """
    Creates a map using Cartopy with colored provinces, country borders,
    coastlines, and land features.
    
    Parameters:
    -----------
    figsize : tuple, optional
        Figure size in inches (width, height). Default is (8, 8)
    extent : list, optional
        Map extent in [lon_min, lon_max, lat_min, lat_max]. 
        Default: [-75, -55, -57, -32]
        
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure object
    ax : matplotlib.axes.Axes
        The axes object
    """
    fig, ax = plt.subplots(figsize=figsize, subplot_kw={'projection': ccrs.Mercator()})
    ax.set_extent(extent, crs=ccrs.PlateCarree())

    # Add basic features
    ax.coastlines(resolution='10m', lw=0.5, alpha=0.7, zorder=3)
    ax.add_feature(high_res_borders, edgecolor='black', linestyle='-', alpha=0.7, lw=0.7, zorder=4)

    # Read provinces shapefile and add colored provinces
    shpfilename = shpreader.natural_earth(resolution='10m',
                                        category='cultural',
                                        name='admin_1_states_provinces')
    
    reader = shpreader.Reader(shpfilename)
    provinces = reader.records()
    
    # Create a colormap with enough colors
    n_colors = 30  # More than enough for provinces
    colors = plt.cm.Set3(np.linspace(0, 1, n_colors))
    
    # Plot each province with a different color
    for i, province in enumerate(provinces):
        if province.attributes['admin'] == 'Argentina':  # Only Argentina's provinces
            geometry = province.geometry
            ax.add_geometries([geometry], ccrs.PlateCarree(),
                            facecolor=colors[i % n_colors],
                            edgecolor='gray',
                            alpha=0.7,
                            linewidth=0.5,
                            zorder=2)

    # Add ticks and labels
    xticks = list(range(extent[0], extent[1] + 1, 5))
    yticks = list(range(extent[2], extent[3] + 1, 5))

    ax.set_xticks(xticks, crs=ccrs.PlateCarree())
    ax.set_yticks(yticks, crs=ccrs.PlateCarree())
    ax.set_xticklabels([f"{x}°" for x in xticks], fontsize=8)
    ax.set_yticklabels([f"{y}°" for y in yticks], fontsize=8)
    ax.spines['geo'].set_visible(False)

    ax.set_xlabel('Longitude', fontsize=8)
    ax.set_ylabel('Latitude', fontsize=8)

    return fig, ax
