from roulement import *

while True:
    groupe = str(input('quel est votre trinome ? : '))
    sem = str(input('quelle semaine (date du lundi) ? : '))

    indice_entete = rlmnt(sem, groupe)
    if indice_entete == [] or indice_entete is None:
        print('Rien !')
    else:
        for k in indice_entete:
            print(entete[k])
