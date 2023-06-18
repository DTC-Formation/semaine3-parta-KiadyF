import random

# Objet participant
class Participant():
    def __init__(self,nom,nbr_tentative = 0):
        self.nom = nom
        self.nbr_tentative = nbr_tentative
    
    def jouer(self):
        nombre_a_deviner = random.randint(1,101)
        le_nombre_est_trouvee = False
        print(f"A toi de jouer {self.nom}")
        while(not le_nombre_est_trouvee):
            reponse = input("Veuillez entrer le nombre à deviner: ")
            if reponse.isnumeric():
                self.nbr_tentative += 1
                if int(reponse) == nombre_a_deviner:
                    le_nombre_est_trouvee = True
                    print(f"\nSuper, vous avez trouver le bon nombre")
                elif int(reponse) < nombre_a_deviner:
                    print("Trop petit, reessayer.")
                else:
                    print("Trop grand, reessayer.")
            else:
                print("Veuiller entrer un chiffre.")
        print("\n\n")
        return 0


#fonction maka ny anaran'ny participants rehetra
def demander_les_noms_des_participants():
    participants = []
    n = 1
    print("Veuillez entrer les noms des participants.\n")
    nom_participant = " "
    while(nom_participant != ""):
        nom_participant = input(f"Nom du participant {n} ou tapez entrer si il n'y a pas:  ")
        n += 1
        if nom_participant != "":
            participants.append(Participant(nom_participant))
    if participants == []:
        print("Aucun participant")
        return demander_les_noms_des_participants()
    print("\n\n")
    return participants

#fonction mijery ny gagnant
def trouver_le_gagnants(liste):
    print("========== Resultat du jeu ==========")
    if len(liste) == 1:
        print(f"Felicitation {liste[0].nom}, vous avez trouvé le bon nombre en juste {liste[0].nbr_tentative} tentatives")
    else:
        for p in liste:
            print(f"{p.nom} a fait {p.nbr_tentative} tentatives")
        gagnant = min(liste, key = lambda p : p.nbr_tentative)
        print(f"\n\nFélicitation, le gagnant est {gagnant.nom}")
    return 0



print("\n\n=========== JEU DEVINETTE, DEVINER LE NOMBRE MAGIQUE ENTRE 1 ET 100 ===========")

liste_participant = demander_les_noms_des_participants()

for p in liste_participant:
    p.jouer()

trouver_le_gagnants(liste_participant)
