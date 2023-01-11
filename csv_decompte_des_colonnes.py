#!/usr/bin/python3
"""
Ce programme compte le nombre de colonnes de tout un fichier csv
    * donne le nombre de colonne
    * avertit si une ligne a un nmobre différent de colonnes
Création du programme le 5 novembre 2019
Dernière modification le 11 janvier 2023
"""
import csv
import argparse #gestion des arguments

parser = argparse.ArgumentParser(description="Compte le nombre de colonnes d'un fichier csv, il affiche le nombre de colonnes et avertit si certaines lignes n'ont pas le même nombre de colonnes.")
parser.add_argument('fichier', help='le fichier dont on doit dénombrer les colonnes')
parser.add_argument('-sep', nargs='?', help="le séparateur du fichier csv, par défaut il s'agit du ;")
parser.add_argument('-n', action='store_true', help="renvoie uniquement le nombre de colonnes, renvoie ERROR si ce nombre n'est pas constant")
args = parser.parse_args()

fichier = args.fichier
if args.sep:
    delimiter = args.sep
else:
    delimiter = ';'

if args.n:
    number_only = True
else:
    number_only = False

premiere_ligne = True
probleme_de_nombre_de_colonnes = False
ligne_en_cours = 1
try:
    with open(fichier, newline='') as f:
        reader = csv.reader(f, delimiter=delimiter, quoting=csv.QUOTE_NONE)
        try:
            for row in reader:
                if premiere_ligne:
                    nbre_colonne = len(row)
                    premiere_ligne = False
                    if not number_only:
                        print("Nombre de colonne du début du fichier = ", nbre_colonne)
                if len(row) != nbre_colonne:
                    probleme_de_nombre_de_colonnes = True
                    nbre_colonne = len(row)
                    if not number_only:
                        print(" -- un nombre de colonne différent ({}) a été détecté à la ligne {}".format(nbre_colonne, ligne_en_cours))
                ligne_en_cours += 1
        except UnicodeDecodeError:
            print(f"\nErreur: Le fichier {fichier} n'est pas encodé en utf8")
            exit()
        except Exception as error :
            print(f"\nErreur: L'erreur suivante s'est produite : ({error}), sur la ligne {ligne_en_cours}")
            exit()
except FileNotFoundError:
    print(f"\nErreur: Le fichier {fichier} n'a pas été trouvé\n")
    exit()
if number_only:
    if probleme_de_nombre_de_colonnes:
        print('ERROR')
    else:
        print(nbre_colonne)
else:
    if probleme_de_nombre_de_colonnes:
        print(f"\nLe fichier {fichier} n'a pas un nombre constant de colonnes sur ses {ligne_en_cours - 1} lignes")
    else:
        print(f"\nLe fichier {fichier} a un nombre constant de colonnes sur ses {ligne_en_cours - 1} lignes :)")
