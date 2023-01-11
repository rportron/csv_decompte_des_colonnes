# csv_decompte_des_colonnes
Permet de :
 * décompter le nombre de colonnes d'un fichier csv
 * Indiquer si le nombre de colonnes varie dans le fichier

## Utilisation
En ligne de commandes
```
./csv_decompte_des_colonnes.py mon_fichier.csv
```

## Point d'attention
Le séparateur par défaut est le point virgule (;)

## Options
### Changement du séparateur par défaut
Avec un fichier dont les champs sont séparés par une virgule :
```
python3 csv_decompte_des_colonnes.py -sep ',' mon_fichier.csv
```
### Pour ne retourner que le nombre de colonnes du fichier
```
python3 csv_decompte_des_colonnes.py -n mon_fichier.csv
```
Si le nombre de colonnes n'est pas constant, ERROR sera renvoyé
