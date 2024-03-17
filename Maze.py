from random import *


class Maze:
    """
    Classe Labyrinthe
    Représentation sous forme de graphe non-orienté
    dont chaque sommet est une cellule (un tuple (l,c))
    et dont la structure est représentée par un dictionnaire
      - clés : sommets
      - valeurs : ensemble des sommets voisins accessibles
    """

    def __init__(self, height, width, empty):
        """
        Constructeur d'un labyrinthe de height cellules de haut
        et de width cellules de large
        Les voisinages sont initialisés à des ensembles vides
        Remarque : dans le labyrinthe créé, chaque cellule est complètement emmurée
        """
        self.height = height
        self.width = width
        self.empty = empty
        if not empty:
            self.neighbors = {(i, j): set() for i in range(height) for j in range(width)}
        else:
            self.neighbors = {(i, j): set((i, j) for i in range(height) for j in range(width)) for i in range(height)
                              for j in range(width)}

    def info(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Affichage des attributs d'un objet 'Maze' (fonction utile pour deboguer)
        Retour:
            chaîne (string): description textuelle des attributs de l'objet
        """
        txt = "**Informations sur le labyrinthe**\n"
        txt += f"- Dimensions de la grille : {self.height} x {self.width}\n"
        txt += "- Voisinages :\n"
        txt += str(self.neighbors) + "\n"
        valid = True
        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in self.neighbors[c1]:
                if c1 not in self.neighbors[c2]:
                    valid = False
                    break
            else:
                continue
            break
        txt += "- Structure cohérente\n" if valid else f"- Structure incohérente : {c1} X {c2}\n"
        return txt

    def __str__(self):
        """
        **NE PAS MODIFIER CETTE MÉTHODE**
        Représentation textuelle d'un objet Maze (en utilisant des caractères ascii)
        Retour:
             chaîne (str) : chaîne de caractères représentant le labyrinthe
        """
        txt = ""
        # Première ligne
        txt += "┏"
        for j in range(self.width - 1):
            txt += "━━━┳"
        txt += "━━━┓\n"
        txt += "┃"
        for j in range(self.width - 1):
            txt += "   ┃" if (0, j + 1) not in self.neighbors[(0, j)] else "    "
        txt += "   ┃\n"
        # Lignes normales
        for i in range(self.height - 1):
            txt += "┣"
            for j in range(self.width - 1):
                txt += "━━━╋" if (i + 1, j) not in self.neighbors[(i, j)] else "   ╋"
            txt += "━━━┫\n" if (i + 1, self.width - 1) not in self.neighbors[(i, self.width - 1)] else "   ┫\n"
            txt += "┃"
            for j in range(self.width):
                txt += "   ┃" if (i + 1, j + 1) not in self.neighbors[(i + 1, j)] else "    "
            txt += "\n"
        # Bas du tableau
        txt += "┗"
        for i in range(self.width - 1):
            txt += "━━━┻"
        txt += "━━━┛\n"

        return txt

    def add_wall(self, c1, c2):

        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"

        # Ajout du mur
        if c2 in self.neighbors[c1]:  # Si c2 est dans les voisines de c1
            self.neighbors[c1].remove(c2)  # on le retire

        if c1 in self.neighbors[c2]:  # Si c3 est dans les voisines de c2
            self.neighbors[c2].remove(c1)  # on le retire

    def remove_wall(self, c1, c2):

        # Facultatif : on teste si les sommets sont bien dans le labyrinthe
        assert 0 <= c1[0] < self.height and \
               0 <= c1[1] < self.width and \
               0 <= c2[0] < self.height and \
               0 <= c2[1] < self.width, \
            f"Erreur lors de l'ajout d'un mur entre {c1} et {c2} : les coordonnées de sont pas compatibles avec les dimensions du labyrinthe"

        # supression du mur
        if not c2 in self.neighbors[c1]:  # Si c2 n'est pas dans les voisines de c1
            self.neighbors[c1].add(c2)  # on l'ajoute

        if not c1 in self.neighbors[c2]:  # Si c3 n'est pas dans les voisines de c2
            self.neighbors[c2].add(c1)  # on l'ajoute

    def get_walls(self):

        txt = str(self.neighbors) + "\n"
        valid = True

        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in self.neighbors[c1]:
                if c1 not in self.neighbors[c2]:
                    valid = False
                    break
            else:
                continue
            break
        txt += "- Structure cohérente\n" if valid else f"- Structure incohérente : {c1} X {c2}\n"

        return txt

    def fill(self):

        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in {(k, l) for k in range(self.height) for l in range(self.width)}:
                self.add_wall(c1, c2)

    def emptyF(self):

        for c1 in {(i, j) for i in range(self.height) for j in range(self.width)}:
            for c2 in {(k, l) for k in range(self.height) for l in range(self.width)}:
                self.remove_wall(c1, c2)

    def get_contiguous_cells(self, c):

        lst = []
        if c[0] == 0:
            if c[1] == 0:
                lst.append((c[0], c[1] + 1))
                lst.append((c[0] + 1, c[1]))

            elif c[1] == self.width - 1:
                lst.append((c[0] + 1, c[1]))
                lst.append((c[0], c[1] - 1))

            else:
                lst.append((c[0], c[1] + 1))
                lst.append((c[0] + 1, c[1]))
                lst.append((c[0], c[1] - 1))

        elif c[0] == self.height - 1:
            if c[1] == 0:
                lst.append((c[0] - 1, c[1]))
                lst.append((c[0], c[1] + 1))

            elif c[1] == self.width - 1:
                lst.append((c[0] - 1, c[1]))
                lst.append((c[0], c[1] - 1))

            else:
                lst.append((c[0] - 1, c[1]))
                lst.append((c[0], c[1] + 1))
                lst.append((c[0], c[1] - 1))

        else:
            if c[1] == 0:
                lst.append((c[0] - 1, c[1]))
                lst.append((c[0], c[1] + 1))
                lst.append((c[0] + 1, c[1]))

            elif c[1] == self.width - 1:
                lst.append((c[0] - 1, c[1]))
                lst.append((c[0] + 1, c[1]))
                lst.append((c[0], c[1] - 1))

            else:
                lst.append((c[0] - 1, c[1]))
                lst.append((c[0], c[1] + 1))
                lst.append((c[0] + 1, c[1]))
                lst.append((c[0], c[1] - 1))

        return lst

    def get_reachable_cells(self, c):

        contigue = self.get_contiguous_cells(c)
        lst = []

        for c2 in contigue:
            if c2 in self.neighbors[c]:
                lst.append(c2)

        return lst

    @classmethod
    def gen_btree(cls, h, w):

        laby = Maze(h, w, empty=False)  # initialisation d'un labyrinthe sans voisins (plein)

        for i in range(h):
            for j in range(w):  # parcour du labyrinthe
                a = randint(0, 25)  # création de a un entier aléatoire

                # Si (i,j) et (i,j+1) sont dans le labyrinthe et a inférieur ou égale a 15 ou que i,j est au bord
                if (a <= 15 and j + 1 <= h - 1) or (i == h - 1 and j + 1 <= h - 1):
                    laby.remove_wall((i, j), (i, j + 1))  # on l'ajoute

                # Si (i,j) et (i+1,j) sont dans le labyrinthe et a supérieur ou égale a 10 ou que i,j est au bord
                if (a >= 10 and i + 1 <= w - 1) or (j == w - 1 and i + 1 <= w - 1):
                    laby.remove_wall((i, j), (i + 1, j))  # on l'ajoute

        return laby

    @classmethod
    def gen_sidewinder(cls, h, w):

        laby = Maze(h, w, empty=False)  # initialisation d'un labyrinthe sans voisins (plein)

        for i in range(h - 1):
            sequence = []  # initialisation de la séquence

            for j in range(w - 1):
                sequence.append((i, j))  # ajout de la cellule dans la séquence
                piece = randint(0, 1)  # tirage Pile ou Face

                if piece == 0:
                    laby.remove_wall((i, j), (i, j + 1))  # si Pile casse mur Est
                else:
                    c1 = sequence[randint(0, len(sequence) - 1)]  # choix de cellule aleatoire parmi la sequence
                    laby.remove_wall(c1, (c1[0] + 1, c1[1]))  # casse le mur sud de la cellule
                    sequence = []  # reinitialisation de la sequence

            sequence.append((i, w - 1))  # ajout derniere cellule dans la sequence
            c2 = sequence[randint(0, len(sequence) - 1)]  # choix de cellule aleatoire parmi la sequence
            laby.remove_wall(c2, (c2[0] + 1, c2[1]))  # casse le mur sud de la cellule
        for k in range(w - 1):
            laby.remove_wall((h - 1, k), (h - 1, k + 1))

        return laby

    @classmethod
    def gen_fusion(cls, h, w):
        # INITIALISATION
        laby = Maze(h, w, empty=False)  # initialisation labyrinth avec mur

        # initialisation des labels associé à leur cellule
        label = []
        a = 0
        for i in range(h):
            for j in range(w):  # parcour des cellules du laby
                label.append([a, (i, j)])  # chaque index de la liste correspond a un label
                a += 1  # ajout de 1 à a

        # initialisation des arêtes
        aretes = []
        for i in range(h):
            for j in range(w):
                voisins = laby.get_contiguous_cells((i, j))  # récupération de la liste des voisins de la cellule (i, j)
                for k in range(len(voisins)):
                    if [voisins[k], (i, j)] not in aretes and [(i, j), voisins[k]] not in aretes:
                        aretes.append([(i, j), voisins[k]])  # ajout des arêtes

        shuffle(aretes)

        # ALGO

        for i in range(len(aretes)):
            # récupération des labels des cellules A et B
            labelA = -1
            labelB = -1
            a = 0

            while (labelA == -1 or labelB == -1) and a < len(label):
                if label[a][1] == aretes[i][0] and labelA == -1:
                    labelA = label[a][0]
                elif label[a][1] == aretes[i][1] and labelB == -1:
                    labelB = label[a][0]
                else:
                    a += 1

            # suppresion du mur et modification des labels
            if labelA != labelB:
                laby.remove_wall(aretes[i][0], aretes[i][1])
                c = 0

                while c < len(label):
                    if label[c][0] == labelA or label[c][0] == labelB:  # pour chaque cellule ayant un label
                        # identique à la cellule A ou à la cellule B
                        label[c][0] = min(labelA, labelB)  # on met le label minimum entre les 2 pour la cellule c
                    c += 1

        return laby

    @classmethod
    def gen_exploration(cls, h, w):

        laby = Maze(h, w, empty=False)  # on initialise un labyrinthe sans voisins
        (i, j) = randint(0, h - 1), randint(0, w - 1)  # selection d'une cellule aleatoire
        visite = [(i, j)]  # ajout de la cellule dans visite
        pile = [(i, j)]  # ajout de la cellule dans pile

        while pile:
            temp = pile[0]  # variable temporaire avec la cellule
            del pile[0]  # suppression de la cellulle dans pile
            voisins = laby.get_contiguous_cells(temp)  # recuperation des voisins de la cellule
            voisinsNonVisite = []

            for k in voisins:
                if k not in visite:
                    voisinsNonVisite.append(k)

            if voisinsNonVisite :
                pile = [temp] + pile
                prochain = randint(0, len(voisinsNonVisite)-1)
                cel = voisinsNonVisite[prochain]  # selection d'un voisin aleatoire
                laby.remove_wall(temp, cel)  # suppression du mur entre la cellule et son voisin choisi
                visite.append(cel)  # ajout du voisin dans visite
                pile = [cel] + pile  # ajout du voisin sur la pile

        return laby

    @classmethod
    def gen_wilson(cls, h, w):
        laby = Maze(h, w, empty=False)  # on initialise un labyrinthe avec voisins
        # récupération de chaque cellulue du labyrinthe
        listeCellule = []
        for i in range(h):
            for j in range(w):
                listeCellule.append((i, j))
        listeCelluleVisitee = []  # liste des cellules visitée

        # choix d'une cellule de départ aléatoire
        celluleAleatoire = choice(listeCellule)
        listeCelluleVisitee.append(celluleAleatoire)

        while len(listeCelluleVisitee) != len(listeCellule):
            celluleDepart = choice(listeCellule)

            while celluleDepart in listeCelluleVisitee:
                celluleDepart = choice(listeCellule)
            listeChemin = [celluleDepart]
            flag = False
            celluleAleatoire = choice(laby.get_contiguous_cells(celluleDepart))

            while not flag and celluleAleatoire not in listeChemin:
                listeChemin.append(celluleAleatoire)
                retour = False

                if listeChemin[-1] not in listeCelluleVisitee:
                    temp = celluleAleatoire
                    if celluleAleatoire not in listeChemin:
                        listeChemin.append(celluleAleatoire)
                        celluleAleatoire = choice(laby.get_contiguous_cells(temp))
                    i = len(listeChemin) - 1
                    compte = 0
                    while celluleAleatoire in listeChemin and compte < len(laby.get_contiguous_cells(temp)):
                        voisins = laby.get_contiguous_cells(listeChemin[i])
                        if compte == 0:
                            shuffle(voisins)
                        if retour:
                            listeChemin.append(listeChemin[i])
                        if compte == len(laby.get_contiguous_cells(temp)):
                            compte = 0
                            i -= 1
                            retour = True
                        else:
                            celluleAleatoire = voisins[compte]
                            compte += 1
                else:
                    listeChemin.append(celluleAleatoire)
                    flag = True

            if flag:
                for i in range(len(listeChemin)-2):
                    if listeChemin[i] not in listeCelluleVisitee:
                        listeCelluleVisitee.append(listeChemin[i])
                    laby.remove_wall(listeChemin[i], listeChemin[i + 1])
                listeCelluleVisitee.sort()

        return laby
