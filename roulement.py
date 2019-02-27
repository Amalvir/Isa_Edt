## Roulement

# Extraction des données
with open("roulement.csv", 'r') as roulement:
    Lroul =[]
    entete = roulement.readline().strip().split('\t')  # On enleve l'en-tete

    for ligne in roulement:
        Lroul.append(ligne.strip().split('\t'))


for i in range(len(Lroul)):
    print(str(i) + " " + str(Lroul[i][0])) # Liste les dates possibles pour faire un choix avec les indices
    for j in range(len(Lroul[i])):
        Lroul[i][j] = Lroul[i][j].split(',')


def roulement(date, kh):
    """Retourne les indices de entete"""

    try:            # Test si on utilise indice ou pas
        date = Lroul[int(date)][0][0]
    except:
        pass

    j = -1
    liste = []
    #f = 0
    for i in range(len(Lroul)):
        if date in Lroul[i][0]:
            j = i
    if j < 0:
        print("Date introuvable !")
        return None
    else:
        #print("j : " + str(j))
        for k in range(len(Lroul[j])):
            try:
                Lroul[j][k].index(str(kh)) # kh dans Lroul[j] ?
                liste.append(k)
                #print("f : " + str(f))
                #print("k : " + str(k[f]))
            except ValueError:
                pass
    return liste


# Interface utilisateur
groupe = str(input('quel est votre trinome ? : '))
sem = str(input('quelle semaine (date du lundi) ? : '))

indice_entete = roulement(sem, groupe)
if indice_entete == [] or indice_entete is None:
    print('Rien !')
else:
    for k in indice_entete:
        print(entete[k])
# Petit teste
