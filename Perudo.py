#!/usr/bin/python3

import math

def exact(n,m,d,l):
    """
    Cette fonction renvoie la probabilité d'avoir exactement 
    k − j (d) fois le nombre l parmi n − m dés
    """
    if l == 1 :
        return(math.comb(n-m,d)*(5**(n-m-(d))/6**(n-m)))
    else :
        return(math.comb(n-m,d)*(2**(n-m-(d))/3**(n-m)))

def normalrules(n,k,m,j,l):
    """
    Cette fonction renvoie la proba que parmi n dés,
    il y a au moins k fois le nombre l ou le paco
    """
    prob = 0
    d = k-j
    for i in range(d,n-m+1):
        prob += exact(n,m,i,l)
    return (prob)

def perudo_display(tot, val, bt, dic, nb_v, pal):
    if pal == 1:
        proba = normalrules(tot, bt, dic, nb_v, 1)
    else  :
        proba = normalrules(tot, bt, dic, nb_v, val)
    return (proba)

def main():
    print("Bienvenue dans l'application calcul de Perudo \n")
    total_dice = int(input("Nombre Total de Dés :\n"))
    value_dice = int(input("Votre Valeur de Dé sur laquelle vous pariez:\n"))
    bet = int(input("Vous pariez qu'il y'a au moins ? :\n"))
    dice = int(input("Combien de dés possédez vous ?\n"))
    nb_value = int(input(f"Combien de {value_dice} avez vous ?\n"))
    palifico = int(input("Est-ce un round palifico 0 si non, 1 si oui\n"))

    print(f"Tu as donc parié qu'il y avait {bet} {value_dice} sur les {total_dice} dés sachant que toi tu possèdes {nb_value} sur tes {dice} dés \n")
    #Assertions Ici
    if total_dice > 30 or total_dice <1 :
        raise ValueError("Le nombre de dés totaux n'est pas bon")
    if value_dice <1 or value_dice>6:
        raise ValueError("Votre valeur de dé n'est pas comprise entre 1 et 6")
    if dice<1 or dice>5:
        raise ValueError("Votre nombre de dés n'est pas bon")
    if nb_value > dice or nb_value <0 :
        raise ValueError(f"Votre nombre de {value_dice} n'est pas bon")
    if bet<0 or bet>total_dice :
        raise ValueError(f"Votre pari n'est pas bon")

    #Vrai calcul ici
    if palifico == 1:
        proba = normalrules(total_dice, bet, dice, nb_value, 1)
    else  :
        proba = normalrules(total_dice, bet, dice, nb_value, value_dice)
    
    print(f"La probabilité que ton pari soit bon est de \033[92m {proba}")

if __name__ == "__main__":
    main()