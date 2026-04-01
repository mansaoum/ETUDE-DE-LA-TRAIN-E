#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt

# Paramètres physiques
rho, nu = 1.225, 1.5e-5
mu = nu * rho

# Géométries: nom -> (L, S)
geoms = {
    'sphere': (0.1, np.pi*(0.05)**2),
    'cylinder': (0.1, 0.02),
    'naca0012': (0.2, 0.0048)
}

def cd_sphere(Re):
    return 24/Re * (1 + 0.15*Re**0.687) if Re < 1e5 else 0.47

def cd_cylinder(Re):
    return 1.2

def cd_naca(Re):
    return 0.01 + 0.1/np.sqrt(Re) if Re < 1e5 else 0.006

def get_cd(geom, Re):
    funcs = {'sphere': cd_sphere, 'cylinder': cd_cylinder, 'naca0012': cd_naca}
    return np.array([funcs[geom](r) for r in Re])

def drag_force(geom, v):
    L, S = geoms[geom]
    Re = rho * v * L / mu
    Cd = get_cd(geom, [Re])[0]
    Fd = 0.5 * rho * v**2 * Cd * S
    return Fd, Cd, Re

def plot_curves():
    Re = np.logspace(0, 7, 100)
    plt.figure(figsize=(10, 6))
    for g in geoms:
        plt.loglog(Re, get_cd(g, Re), label=g.capitalize(), lw=2)
    plt.xlabel('Re'); plt.ylabel('Cd')
    plt.title('Courbes théoriques Cd = f(Re)')
    plt.legend(); plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("=== Étude de la Traînée Aérodynamique ===")

    # Exemple de calcul
    v = 10
    print(f"Forces à {v} m/s:")
    for g in geoms:
        Fd, Cd, Re = drag_force(g, v)
        print(f"  {g}: Fd={Fd:.3f}N, Cd={Cd:.4f}, Re={Re:.1e}")

    # Graphique
    plot_curves()