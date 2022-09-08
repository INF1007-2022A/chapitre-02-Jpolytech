#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    x = input("entrer une lettre en minuscule :")
    print("Le code ASCII de ",x," est : ",ord(x))
    x = ord(x) - 32
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
