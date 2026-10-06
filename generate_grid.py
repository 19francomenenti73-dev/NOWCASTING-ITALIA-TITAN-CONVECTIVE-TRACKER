import os
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

os.makedirs("immagini", exist_ok=True)

def genera_isometric_cella_immagine(max_dbz, percorso_di_output):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    dimensione_griglia = 10
    X = np.linspace(0, dimensione_griglia, 11)
    Y = np.linspace(0, dimensione_griglia, 11)
    X, Y = np.meshgrid(X, Y)

    # Calcolo della superficie 3D della cella
    Z = np.exp(-((X - 5)**2 + (Y - 5)**2) / 10.0) * (max_dbz / 1.5)

    # Nota: rimosso 'rasterized=True' per evitare l'errore di incompatibilità
    ax.plot_surface(X, Y, Z, cmap='gist_nipy_spectral', rstride=1, cstride=1, linewidth=0, antialiased=False)
    
    ax.axis('off')
    ax.view_init(elev=35, azim=45)

    plt.savefig(percorso_di_output, bbox_inches='tight', dpi=150, transparent=True)
    plt.close()

def genera_sample_json():
    percorso_json = "cells.json"
    dati_di_esempio = [
        {
            "id": "cella_01",
            "lat": 45.4642,
            "lon": 9.1900,
            "max_dbz": 68,
            "vil": "48 kg/m²",
            "eta": "35 minuti",
            "velocity": "55 km/h",
            "severity": "Alto",
            "hail_risk": "Elevato",
            "image_path": "immagini/cell_sample_01.png",
            "history_path": [
                [45.2000, 8.9000],
                [45.3300, 9.0500],
                [45.4642, 9.1900]
            ],
            "forecast_path": [
                [45.4642, 9.1900],
                [45.6000, 9.3500],
                [45.7500, 9.500]
            ],
            "cep_ring": {
                "lat": 45.7500,
                "lon": 9.500,
                "radius_m": 12000
            }
        }
    ]
    with open(percorso_json, 'w', encoding='utf-8') as f:
        json.dump(dati_di_esempio, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    genera_isometric_cella_immagine(68, "immagini/cell_sample_01.png")
    genera_sample_json()
    
