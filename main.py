from Maze import *

""" PARTIE 3 """
laby = Maze(4, 4, empty=False)
print(laby.info())
print(laby)

laby.neighbors = {
    (0, 0): {(1, 0)},
    (0, 1): {(0, 2), (1, 1)},
    (0, 2): {(0, 1), (0, 3)},
    (0, 3): {(0, 2), (1, 3)},
    (1, 0): {(2, 0), (0, 0)},
    (1, 1): {(0, 1), (1, 2)},
    (1, 2): {(1, 1), (2, 2)},
    (1, 3): {(2, 3), (0, 3)},
    (2, 0): {(1, 0), (2, 1), (3, 0)},
    (2, 1): {(2, 0), (2, 2)},
    (2, 2): {(1, 2), (2, 1)},
    (2, 3): {(3, 3), (1, 3)},
    (3, 0): {(3, 1), (2, 0)},
    (3, 1): {(3, 2), (3, 0)},
    (3, 2): {(3, 1)},
    (3, 3): {(2, 3)}
}

print(laby)

laby.neighbors[(1, 3)].remove((2, 3))
laby.neighbors[(2, 3)].remove((1, 3))
print(laby)

laby.neighbors[(1, 3)].add((2, 3))
laby.neighbors[(2, 3)].add((1, 3))
print(laby)

laby.neighbors[(1, 3)].remove((2, 3))
print(laby)
print(laby.info())

laby.neighbors[(2, 3)].remove((1, 3))

c1 = (1, 3)
c2 = (2, 3)
if c1 in laby.neighbors[c2] and c2 in laby.neighbors[c1]:
    print(f"Il n'y a pas de mur entre {c1} et {c2} car elles sont mutuellement voisines")
elif c1 not in laby.neighbors[c2] and c2 not in laby.neighbors[c1]:
    print(
        f"Il y a un mur entre {c1} et {c2} car {c1} n'est pas dans le voisinage de {c2} et {c2} n'est pas dans le voisinage de {c1}")
else:
    print(f"Il y a une incohérence de réciprocité des voisinages de {c1} et {c2}")

c1 = (1, 3)
c2 = (2, 3)
if c1 in laby.neighbors[c2] and c2 in laby.neighbors[c1]:
    print(f"{c1} est accessible depuis {c2} et vice-versa")
elif c1 not in laby.neighbors[c2] and c2 not in laby.neighbors[c1]:
    print(f"{c1} n'est pas accessible depuis {c2} et vice-versa")
else:
    print(f"Il y a une incohérence de réciprocité des voisinages de {c1} et {c2}")

L = []
for i in range(laby.height):
    for j in range(laby.width):
        L.append((i, j))
print(f"Liste des cellules : \n{L}")

laby = Maze(4, 4, empty=True)
print(laby)

laby = Maze(4, 4, empty=False)
print(laby)

""" PARTIE 4 """
laby = Maze(5, 5, empty=True)
print(laby)

laby.add_wall((0, 0), (0, 1))
print(laby)

laby = Maze(5, 5, empty=True)
laby.fill()
print(laby)

laby.remove_wall((0, 0), (0, 1))
print(laby)

laby.emptyF()
laby.add_wall((0, 0), (0, 1))
laby.add_wall((0, 1), (1, 1))
print(laby)

print(laby.get_walls())

print(laby.get_contiguous_cells((0, 1)))

print(laby.get_reachable_cells((0, 1)))

""" PARTIE 5 """
laby = Maze.gen_btree(4, 4)
print(laby)

laby = Maze.gen_sidewinder(4, 4)
print(laby)

laby = Maze.gen_fusion(15, 15)
print(laby)

laby = Maze.gen_exploration(15, 15)
print(laby)

laby = Maze.gen_wilson(15, 15)
print(laby)

"""Partie 6"""
laby = Maze(4, 4, empty=True)
print(laby.overlay({
    (0, 0): 'c',
    (0, 1): 'o',
    (1, 1): 'u',
    (2, 1): 'c',
    (2, 2): 'o',
    (3, 2): 'u',
    (3, 3): '!'}))

laby = Maze(4, 4, empty=True)
path = {(0, 0): '@',
        (1, 0): '*',
        (1, 1): '*',
        (2, 1): '*',
        (2, 2): '*',
        (3, 2): '*',
        (3, 3): '§'}
print(laby.overlay(path))


laby = Maze.gen_fusion(15, 15)
solution = laby.solve_dfs((0, 0), (14, 14))
str_solution = {c: '*' for c in solution}
str_solution[(0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))

laby = Maze.gen_exploration(15, 15)
solution = laby.solve_bfs((0, 0), (14, 14))
str_solution = {c: '*' for c in solution}
str_solution[(0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))

"""
8.1 : À faire (question ouverte)
Imaginer une ou plusieurs manières de compliquer les labyrinthes générés.

Afin de compliquer les labyrinthes générés, il est possible d'utiliser plusieurs méthodes :

- Introduire des pièges ou des obstacles : On pourrait ajouter des zones dans le labyrinthe qui représentent des 
pièges ou des obstacles, obligeant ainsi le joueur à trouver un chemin spécifique pour les contourner ou les éviter. 
Nous pensions notamment à des caisses, des balles, des bombes... Nous pourrions même rajouter des adversaires ou des 
monstres à éviter avec une notion de vie qui diminue.

- Augmenter la complexité des passages : Au lieu d'avoir des passages simples entre les cellules, on 
pourrait introduire des passages étroits, des passages en zigzag ou des passages avec des portes à déverrouiller, 
rendant la navigation plus difficile.

- Incorporer des zones de téléportation : Des portails, comme dans le jeu Portal 2. On pourrait rajouter des zones 
dans le labyrinthe qui téléportent le joueur vers un autre emplacement aléatoire du labyrinthe, ce qui ajouterait 
une dimension de surprise et de défi.

- Implémenter des mécanismes de temps ou de limite de mouvements : Introduire un élément temporelle ou limiter le 
nombre de mouvements autorisés pour résoudre le labyrinthe, ce qui obligerait à prendre des décisions stratégiques 
plus rapidement.

- Ajouter des énigmes ou des puzzles : Intégrer des énigmes ou des puzzles dans certaines parties du labyrinthe, 
nécessitant au joueur de résoudre des problèmes logiques ou mathématiques pour avancer. Cela boost l'apprentissage, 
tout en augmentant significativement la difficulté.
"""