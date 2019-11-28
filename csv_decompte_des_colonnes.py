#!/usr/bin/python3
"""
Ce programme compte le nombre de colonnes de tout un fichier csv
    * donne le nombre de colonne
    * avertit si une ligne a un nmobre différent de colonnes
Création du programme le 5 novembre 2019
Dernière modification le 28 novembre 2019
"""
import csv
import argparse #gestion des arguments

parser = argparse.ArgumentParser(description="Compte le nombre de colonnes d'un fichier csv")
parser.add_argument('fichier', help='le fichier dont on doit dénombrer les colonnes')
parser.add_argument('-sep', nargs='?', help="le séparateur du fichier csv, par défaut il s'agit du ;")
args = parser.parse_args()

fichier = args.fichier
if args.sep:
    delimiter = args.sep
else:
    delimiter = ';'

print("\nCe programme compte le nombre de colonnes d'un fichier csv, il affiche le nombre de colonnes et avertit si certaines lignes n'ont pas le même nombre de colonnes\n")

premiere_ligne = True
probleme_de_nombre_de_colonnes = False
ligne_en_cours = 1
with open(fichier, newline='') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            if premiere_ligne:
                nbre_colonne = len(row)
                premiere_ligne = False
                print("Nombre de colonne du début du fichier = ", nbre_colonne)
            if len(row) != nbre_colonne:
                probleme_de_nombre_de_colonnes = True
                nbre_colonne = len(row)
                print(" -- un nombre de colonne différent ({}) a été détecté à la ligne {}".format(nbre_colonne, ligne_en_cours))
            ligne_en_cours += 1
if probleme_de_nombre_de_colonnes:
    print("\nLe fichier {} n'a pas un nombre constant de colonnes :(".format(fichier))
else:
    print("\nLe fichier {} a un nombre constant de colonnes :)".format(fichier))
