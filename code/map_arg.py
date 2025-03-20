from functions import plot_map_with_admin_boundaries

save_path = 'exported_figs/mapa_arg.png'

fig, ax = plot_map_with_admin_boundaries()
fig.savefig(save_path, dpi=300, bbox_inches='tight')
