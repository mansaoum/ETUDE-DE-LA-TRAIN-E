#  Étude Expérimentale de la Traînée Aérodynamique

---

## 1. Contexte et objectif

La traînée aérodynamique est la force qui s'oppose au mouvement d'un corps se déplaçant dans un fluide. C'est un paramètre **fondamental en aéronautique** : minimiser la traînée d'un avion, c'est réduire sa consommation de carburant, augmenter sa vitesse maximale et améliorer ses performances globales.

L'objectif du projet est de **mesurer expérimentalement** les forces de traînée sur différentes géométries, de **tracer les courbes caractéristiques** Cd = f(Re), et de **comparer** les résultats aux lois théoriques de la dynamique des fluides.

---

## 2. Fondements physiques

### La force de traînée

La force de traînée exercée par un fluide sur un corps est donnée par :

$$F_d = \frac{1}{2} \rho v^2 C_d S$$

Avec :
- **ρ** = masse volumique de l'air (kg/m³)
- **v** = vitesse de l'écoulement (m/s)
- **Cd** = coefficient de traînée (sans dimension)
- **S** = surface de référence du corps (m²)

Le **coefficient de traînée Cd** est la grandeur centrale du projet. Il caractérise la résistance aérodynamique d'une géométrie indépendamment de sa taille et de la vitesse d'écoulement.

### Le nombre de Reynolds

Le comportement de l'écoulement autour d'un corps dépend du **nombre de Reynolds** :

$$Re = \frac{\rho v L}{\mu} = \frac{v L}{\nu}$$

Avec :
- **L** = longueur caractéristique du corps (m)
- **μ** = viscosité dynamique de l'air (Pa·s)
- **ν** = viscosité cinématique de l'air ≈ 1,5 × 10⁻⁵ m²/s

Le nombre de Reynolds traduit le rapport entre les **forces d'inertie** et les **forces visqueuses** :
- **Re faible** → écoulement laminaire, forces visqueuses dominantes
- **Re élevé** → écoulement turbulent, forces d'inertie dominantes

C'est lui qui gouverne la valeur de Cd et la nature de l'écoulement autour du corps.

---

## 3. Les régimes d'écoulement et lois théoriques

### Régime de Stokes (Re < 1)
À très faible Reynolds, l'écoulement est purement laminaire et la traînée est dominée par la viscosité. La loi de Stokes donne pour une sphère :

$$F_d = 6\pi\mu R v \quad \Rightarrow \quad C_d = \frac{24}{Re}$$

### Régime intermédiaire (1 < Re < 10⁵)
Le Cd diminue progressivement avec Re. Pour une sphère, on utilise la **corrélation de Schiller-Naumann** :

$$C_d = \frac{24}{Re}\left(1 + 0{,}15 \cdot Re^{0{,}687}\right)$$

### Régime turbulent — Crise de traînée (Re ≈ 3×10⁵)
Au-delà d'un certain Reynolds, la couche limite passe brutalement de **laminaire à turbulente**. La séparation de la couche limite se produit plus tard sur le corps, réduisant le sillage et donc le Cd. C'est la **crise de traînée** :
- Avant la crise : Cd ≈ 0,47 pour une sphère
- Après la crise : Cd chute à ≈ 0,10

### Profil NACA 0012
Le profil NACA 0012 est un profil symétrique de référence en aéronautique. À faible angle d'attaque, sa traînée est très faible (Cd ≈ 0,006 à Re = 10⁶) car sa forme est optimisée pour maintenir l'écoulement attaché le plus longtemps possible.

---

## 4. Protocole expérimental

### Géométries testées
Trois géométries ont été testées pour couvrir des comportements aérodynamiques très différents :

| Géométrie | Cd théorique attendu | Comportement |
|---|---|---|
| Sphère | 0,47 (laminaire) | Crise de traînée visible |
| Cylindre | 1,0 – 1,2 | Sillage de Von Kármán |
| Profil NACA 0012 | 0,006 – 0,012 | Très faible traînée |



### Dispositif de mesure
- **Couloir d'air instrumenté** à vitesse contrôlée
- **Capteur de force** pour mesurer F_d directement
- **Anémomètre** pour mesurer la vitesse d'écoulement v
- **Calcul de Re** à partir de v, L et ν de l'air

### Déroulement
Pour chaque géométrie, la vitesse d'écoulement est variée par paliers. À chaque palier, on mesure F_d, on calcule Re et on en déduit Cd via :

$$C_d = \frac{2 F_d}{\rho v^2 S}$$

---

## 5. Traitement des données sous Python

Les données brutes ont été traitées sous **Python** avec numpy et matplotlib :

### Moyennage et nettoyage
Pour chaque vitesse, plusieurs mesures sont effectuées et moyennées pour réduire le bruit de mesure :

$$\bar{F_d} = \frac{1}{n}\sum_{i=1}^{n} F_{d,i}$$

### Régression polynomiale
Une régression polynomiale est appliquée sur les courbes Cd = f(Re) pour lisser les données expérimentales et en extraire la tendance :

$$C_d(Re) = a_0 + a_1 Re + a_2 Re^2 + \ldots$$

### Intervalles de confiance à 95 %
L'incertitude sur chaque mesure est quantifiée par un **intervalle de confiance à 95 %** basé sur l'écart-type :

$$IC_{95\%} = \bar{F_d} \pm 1{,}96 \cdot \frac{\sigma}{\sqrt{n}}$$

---

## 6. Résultats et validation

Les courbes expérimentales Cd = f(Re) ont été comparées aux lois théoriques :

| Géométrie | Écart moyen mesuré | Observation |
|---|---|---|
| Sphère | < 9 % | Crise de traînée bien visible |
| Cylindre | < 9 % | Sillage de Von Kármán identifié |
| NACA 0012 | < 9 % | Très bon accord avec les données NACA |

L'écart moyen global reste **inférieur à 9 %** sur l'ensemble des configurations, ce qui est cohérent avec les incertitudes expérimentales liées aux effets de bord et à la turbulence parasite du couloir d'air.

---

## 7. Analyse critique des erreurs

Plusieurs sources d'erreur ont été identifiées et discutées :

- **Effets de bord** : les parois du couloir d'air perturbent l'écoulement autour des maquettes
- **Turbulences parasites** : le couloir d'air n'est pas parfaitement laminaire en entrée
- **Précision du capteur de force** : sensibilité limitée aux faibles vitesses
- **Alignement des maquettes** : un léger angle d'attaque non nul fausse la mesure de Cd pur

Des **améliorations proposées** : grille de lissage en entrée de veine, capteur de force plus précis, système de guidage angulaire des maquettes.

---

## 8. Compétences mobilisées

- **Dynamique des fluides** : traînée, nombre de Reynolds, couche limite, régimes laminaire/turbulent
- **Métrologie** : mesure expérimentale, incertitudes, intervalles de confiance
- **Traitement de données** : Python (numpy, matplotlib), régression polynomiale
- **CAO** : modélisation des maquettes sous CATIA V5 et SolidWorks
- **Analyse critique** : identification des sources d'erreur et propositions d'amélioration

---

## 9. Implémentation informatique

Le projet inclut une implémentation en Python pour les calculs théoriques et la visualisation 


### Fonctionnalités du code
- Calcul des coefficients de traînée selon les lois théoriques
- Simulation de données expérimentales avec bruit
- Calcul d'intervalles de confiance
- Génération de graphiques Cd = f(Re)
- Comparaison théorie/expérience