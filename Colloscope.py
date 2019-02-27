## Colloscope PCS3:

# fichiers et création de listes:
colloscope=open("colloscope.txt", 'r')
horaire=open("horaire.txt", 'r')

c=[]
for ligne in colloscope:
    c.append(ligne.split())
colloscope.close()

h=[]
for ligne in horaire:
    h.append(ligne.split())
horaire.close()


matiere=c[0]
c[0]=[]
for i in range (len(matiere)):
    if i!=0 and i%2==0:
        c[0].append(matiere[i-1]+matiere[i])
matiere=c[0] 
     
semaine=[]
trinome=[]
for i in range (1,len(c)):
    semaine.append(c[i][0])
    t=[]
    for j in range (1,len(c[0])+1):
        t.append(c[i][j])
    trinome.append(t)

heure=[]
for i in range (len(h)):
    if h[i][0]== 'LV':
        h[i][0]='An'
    h[i][0]+=h[i][1]
    t=[]
    for j in range (len(h[0])):
        if j!=1:
            t.append(h[i][j])
    heure.append(t)

# fonctions:
def kholle(sem,groupe):
    '''atribut les kholles pour la semaine à un trinome'''
    kh=[]
    for i in range (len(semaine)):
        for j in range (len(matiere)):
            if semaine[i]==sem and trinome[i][j]==groupe:
                kh.append(matiere[j])
    return kh
    
def transfo (L):
    '''convertit une liste en chaine de caractère'''
    ch=''
    for x in L:
        ch+=x +' '
    return ch

def temps (sem, groupe):
    '''associe une heure a chaque colle'''
    tps=[]
    reponse=''
    kh=kholle(sem,groupe)
    for i in range(len(heure)):
        for j in range (len(kh)):
            if kh[j]==heure[i][0]:
                tps.append(heure[i])
    return tps

#interface avec l'utilisateur:
groupe=str(input('quel est votre trinome? '))
sem=str(input('quelle semaine (date du lundi)? '))
tps=temps(sem,groupe)
for i in range (len(tps)):
    print('\n'+(transfo(tps[i])))