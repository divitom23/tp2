#cree par Max divito
#cree en 2023
#projet devinette tp 2

#je defini mes variables
from random import randint as e
#fonction des brones

choix = 1

# je imput rien dans la fonction
# je recoit un output du nombre random entre le maximum et le minimum choisit par lutilisateur
# la fonction va choisir un nombre qui va etre deviner par l'utilisateur
def borne():
    y = int(input("quel est le maximum du range de devinette"))
    z = int(input("quel est le minimum du range de devinette"))
    print("j'ai choisit un numero entre %d et %d, deviner le" % (z, y))
    x1 = e(z, y)
    return x1

#boucle qui va redmarrer le jeu si vous choisisser de rejouer a la devinnette
while choix == 1:

    x = borne()



    NbrEssais = 0
    essai = None



    #boucle qui vous permet de deviner la reponse et desinger si votre essai est plus grande ou plus petit que la reponse
    while essai != x:

        NbrEssais = NbrEssais + 1
        essai = int(input("votre reponse:"))
        if essai > x:
                print("votre reponse est trop elever, essailler de deviner des numeros plus basses")
        elif essai < x:
                print("votre numero est trop basses, essailler de deviner un numero plus elever")
    #choix de rejouer ou de quitter apre avoir gagner.
    print("WOW that was very cool")
    print("vous avez fait %d essais" %(NbrEssais))
    choix = int(input("1: rejouer?\n 2: quitter le jeu?"))


print('bye bye')