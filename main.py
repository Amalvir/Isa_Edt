from roulement import *
from colloscope import *

while True:
    groupe = str(input('quel est votre trinome ? : '))
    sem = str(input('quelle semaine (date du lundi) ? : '))

    # Test si on utilise l'indice ou pas puis convertit si oui
    try:
        sem = Lroul[int(sem)][0][0]
    except ValueError:
        pass

    indice_entete = rlmnt(sem, groupe)
    tps = temps(sem, groupe)
    if indice_entete == [] or indice_entete is None:
        print('Rien !')
    else:
        # Partie de l'edt
        print("\nEmploi du temps:")
        for k in indice_entete:
            print(entete[k], end='\t')

        # Partie des colles
        print("\n\nColle:")
        for i in range(len(tps)):
            print((transfo(tps[i])), end='\t')
        print("\n")
