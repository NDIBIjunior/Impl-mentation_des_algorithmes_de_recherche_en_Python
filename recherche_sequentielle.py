liste = input("Bonjour\nVeuillez entrer les éléments de votre liste separés d'un espace: ")
liste = liste.split(" ")

element = input("Veuillez entrer l'élément recherché: ")

i= int(0)
position = int(0)
trouve = bool

for elt in liste:
    position = position+1
    if(elt == element):
        trouve = True
        i = position

if(trouve == True):
    print("L'élément '",element,"'se trouve dans la liste à la position", i)
else:
    print("L'élément '", element,"'ne se trouve pas dans la liste !!")
  
