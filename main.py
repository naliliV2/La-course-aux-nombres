def recursivity(liste, number):
    for i in range liste:

def main():
    nb = int(input("Donner n \n>>> "))
    liste = []
    for i in range(1, nb+1):
        liste.append(i)
    
    for first_number in liste:
        liste_temp = liste.copy
        first_number_choise = liste_temp.pop(first_number)
        recursivity(liste_temp, first_number_choise)

    





if __name__ == "__main__":
    main()