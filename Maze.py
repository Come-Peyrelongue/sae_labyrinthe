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
        laby = Maze(h, w, empty=False)  # initialisation labyrinthe avec mur
        label = []  # label = liste vide
        a = 0  # initialisation de a à 0
        for i in range(h):
            for j in range(w):  # parcour des cellules du laby
                label.append([a, (i, j)])  # chaque index du dictionnaire correspond a un label
                a += 1  # ajout de 1 à a
        shuffle(label)  # mélange de la liste
        k = 0

        # ALGO
        while k < len(label):  # pour chaque cellule de la liste
            l = 0
            modif = False  # nombre de modifications max par cellule k = 1
            while l < len(label) and not modif:  # pour chaque cellule de la liste
                if (label[l][1] in laby.get_contiguous_cells(label[k][1])
                        and label[k][0] != label[l][0]):  # si une cellule est voisine avec une autre et ne possède
                    # pas le même label
                    laby.remove_wall(label[k][1], label[l][1])  # retirer le mur entre elle

                    # Modification du label
                    b = 0
                    while b < len(label):
                        if label[b][0] == label[l][0] or label[b][0] == label[k][0]:  # pour chaque cellule ayant un
                            # label identique à k ou à l
                            label[b][0] = min(label[l][0], label[k][0])  # on met le label minimum entre les 2 pour
                            # la cellule b
                        b += 1
                    modif = True
                l += 1
            k += 1
        return laby  # on retourne le labyrinthe

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

            if voisins not in visite:
                pile = [temp] + pile  # ajout de la cellule sur la pile
                for k in voisins:
                    if k in visite:
                        del k  # suppression des voisins visite dans voisins
                cel = voisins[randint(0, len(voisins) - 1)]  # selection d'un voisin aleatoire
                laby.remove_wall(temp, cel)  # suppression du mur entre la cellule et son voisin choisi
                visite.append(cel)  # ajout du voisin dans visite
                pile = [cel] + pile  # ajout du voisin sur la pile

        return laby

    """@classmethod
    def gen_wilson(cls, h, w):

        laby = Maze(h, w, empty=False)  # on initialise un labyrinthe sans voisins
        (i, j) = randint(0, h - 1), randint(0, w - 1)  # selection d'une cellule aleatoire

        marque = []  # initialisation de la liste marque
        for k in range(h):
            ligneMarque = []
            for l in range(w):
                ligneMarque.append(False)
            marque.append(ligneMarque)  # ajout de toute les cellules en False a marque
        marque[i][j] = True  # passage de la cellule (i,j) a True dans marque
        visite = []

        while False in marque:
            depart = randint(0, h - 1), randint(0, w - 1)  # selection d'une cellule de depart aleatoire
            cel1 = depart
            temp = [cel1]       # initialisation d'une liste temporaire avec la cellule de depart

            while not marque[cel1[0]][cel1[1]] or cel1 not in visite:
                voisins = laby.get_contiguous_cells(cel1)  # recuperation des voisins de la cellule
                cel1 = voisins[randint(0, len(voisins) - 1)]  # selection d'un voisin aleatoire
                laby.remove_wall(cel1, cel2)  # suppression du mur entre la cellule et son voisin choisi
                temp.append(cel2)       # ajout de la cellule 2 dans la liste temporaire
                cel1 = cel2     # initalise la 1ere cellule avec la 2e pour la prochaine boucle

                if cel2 in visite:      # cas du serpent qui se mort la queue
                    del temp        # supression des passage dans la liste
                else:
                    for n in range(len(temp)):
                        visite.append(temp[n])      # ajout du chemin dans visite

                for i in range(1, len(visite)):
                    temp2 = visite[i]
                    marque[temp2[0]][temp2[1]] = True     # marquage des"""


"""                    laby.remove_wall(visite[i - 1], temp)"""
