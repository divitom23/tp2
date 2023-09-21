#cree par Max divito
#cree en 2023
#projet devinette tp 2

#je defini mes variables
from random import randint as e
#fonction des brones
def borne():
    y = int(input("quel est le maximum du range de devinette"))
    z = int(input("quel est le minimum du range de devinette"))
    print("j'ai choisit un numero entre %d et %d, deviner le" % (z, y))
    x1 = e(z, y)
    return x1
x = borne()
print(x)

loop = 0
NbrEssais = 1



#j'installe ma boucle
while loop == 0:
    essai = int(input("votre reponse:"))
    #si tu reussit
    if essai == x:
        print("WOW that was very cool")
        loop = loop + 1
        print("vous avez fait %d essais" %(NbrEssais))

    else:
        print("skill issue, you need a tissue, try again")
        NbrEssais = NbrEssais +1
        if essai > x:
            print("votre reponse est trop elever, essailler de deviner des numeros plus basses")
        else:
            print("votre numero est trop basses, essailler de deviner un numero plus elever")



