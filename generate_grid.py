import os
import numpy as np
import matplotlib.pyplot as plt

# Crea la cartella images se non esiste
os.makedirs("images", exist_ok=True)

def generate_isometric_cell_image(max_dbz, output_path):
    fig, ax = plt.subplots(figsize=(6, 5), subplot_kw={'projection': '3d'})
    
    # Griglia 18x18 per la proiezione isometrica
    grid_size = 18
    x = np.arange(0, grid_size, 1)
    y = np.arange(0, grid_size, 1)
    X, Y = np.meshgrid(x, y)
    
    # Simulazione del profilo verticale (Z) basato sulla riflettività reale
    # Il picco centrale riflette la severità della cella (es. 68 dBZ)
    Z = np.exp(-((X - grid_size/2)**2 + (Y - grid_size/2)**2) / 12.0) * (max_dbz / 4.5)
    
    # Plot della superficie isometrica con scala colori radar standard (Verde -> Giallo -> Rosso -> Magenta)
    surf = ax.plot_surface(X, Y, Z, cmap='nipy_spectral', edgecolor='none', alpha=0.9, rstride=1, cstrides=1)
    
    # Pulizia dell'aspetto per renderlo simile a un pannello tecnico strumentale
    ax.set_axis_off()
    ax.view_init(elev=35, azim=45) # Inclinazione isometrica
    
    # Salva l'immagine trasparente e pulita
    plt.savefig(output_path, bbox_inches='tight', dpi=150, transparent=True)
    plt.close()
    print(f"Immagine isometrica generata con successo in: {output_path}")

if __name__ == "__main__":
    # Esempio basato su una cella critica a 68 dBZ
    generate_isometric_cell_image(68, "images/cell_sample_01.png")
  
