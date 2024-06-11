liste = input("Bonjour\nVeuillez entrer les éléments de votre liste separés d'un espace\n(assurer vous qu'ils soient classés par ordre croissant): ")
liste = liste.split(" ")
element = input("Veuillez entrer l'élément recherché: ")

taille = len(liste)
milieu = int()
min, max = 1, taille
trouvee = False

while min <= max and trouvee == False:
    milieu = (min + max)//2
    if (liste[milieu-1] == element):
        trouvee = True
        position = milieu
        print("L'élément '",element, "'a été trouvé dans le tableau a la position",position)

    if(liste[milieu-1] < element):
        min = milieu+1
        if(min == max-1 and liste[min] == element):
            print("L'élément '",element, "'a été trouvé dans le tableau a la position",min)


    if(liste[milieu-1] > element):
        max = milieu-1
        if(min == max and liste[max] == element):
            print("L'élément '",element, "'a été trouvé dans le tableau a la position",min)

if(trouvee == False):
    print("L'élément '", element,"'ne se trouve pas dans la liste !!")

    
