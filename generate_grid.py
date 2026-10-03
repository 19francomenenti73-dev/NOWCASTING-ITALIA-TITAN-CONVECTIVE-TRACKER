import os
import json
import matplotlib
matplotlib.use('Agg')  # Indispensabile per ambienti server headless
import numpy as np
import matplotlib.pyplot as plt

print("Inizio generazione griglia isometrica 3D...")
os.makedirs("images", exist_ok=True)

def generate_isometric_cell_image(max_dbz, output_path):
    fig, ax = plt.subplots(figsize=(6, 5), subplot_kw={'projection': '3d'})
    
    grid_size = 18
    x = np.arange(0, grid_size, 1)
    y = np.arange(0, grid_size, 1)
    X, Y = np.meshgrid(x, y)
    
    # Profilo verticale della cella basato sulla riflettività
    Z = np.exp(-((X - grid_size/2)**2 + (Y - grid_size/2)**2) / 12.0) * (max_dbz / 4.5)
    
    ax.plot_surface(X, Y, Z, cmap='nipy_spectral', edgecolor='none', alpha=0.9, rstride=1, cstrides=1)
    ax.set_axis_off()
    ax.view_init(elev=35, azim=45)
    
    plt.savefig(output_path, bbox_inches='tight', dpi=150, transparent=True)
    plt.close()
    print(f"Immagine isometrica salvata con successo in: {output_path}")

def generate_sample_json():
    json_path = "cells.json"
    sample_data = [
        {
            "lat": 41.9028,
            "lon": 12.4964,
            "max_dbz": 68,
            "velocity": "45 km/h NE",
            "severity": "Alta (Severa)",
            "hail_risk": "Elevato (> 3cm)",
            "vil": "48 kg/m²",
            "eta": "15 min",
            "image_path": "images/cell_sample_01.png",
            "history_path": [[41.80, 12.40], [41.85, 12.45], [41.9028, 12.4964]],
            "forecast_path": [[41.9028, 12.4964], [41.95, 12.55], [42.00, 12.60]],
            "cep_ring": {
                "lat": 42.00,
                "lon": 12.60,
                "radius_m": 5000
            }
        }
    ]
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=4)
    print("File cells.json generato/aggiornato con successo.")

if __name__ == "__main__":
    generate_isometric_cell_image(68, "images/cell_sample_01.png")
    generate_sample_json()
    
