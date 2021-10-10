def create_list_number(number, list_number =[]): 
    '''
    Create the list of number

    Requiere:       Type:       Explain: 
    Number          int         Define the length of the list, start at 1 to finish at number.

    Optional:
    list_number     list        Create a variable list. (Yes i know, it's a bad location, but... i'm god :p )
    '''

    for i in range(1, number+1):
        list_number.append(i)
    return list_number

def recursivity(list_number, list_number_used, max_sum = 0 , list_max_sum = [], max_lenght = 0, list_max_lenght = []):
    '''
    Test all possibility for find the best sum of all. 

    Requiere:           Type:       Explain: 
    list_number         list        List of number remaining
    list_number_used    list        List of number used, [-1] = the last used. 

    Optional: 
    max_sum             int         The max sum find by the algorithm
    list_max_sum        list        The list of the max sum.

    max_lenght          int         The max sum find by the algorithm
    list_max_lenght     list        The list of the max sum
    '''

    if len(list_number) > 0:
        for number_test in list_number:
        
            if number_test > list_number_used[-1]:
                if number_test % list_number_used[-1] == 0:
                    multiple = True
                else:
                    multiple = False
        
            elif number_test < list_number_used[-1]:
                if list_number_used[-1] % number_test == 0:
                    multiple = True
                else:
                    multiple = False
            
            else: #Ne devrait jamais arrivé
                print("Fatal Error : number test and last number is egal.")
                print(number_test, list_number_used, list_number)
                exit()

            if multiple == True:
                for i in range(len(list_number)): #Search number test in list_number
                    if number_test == list_number[i]:
                        copy_list_number = list_number.copy() #Je fais une copie, pour avoir toujours la liste original complète.
                        copy_list_number.pop(i)
                        break
                copy_list_number_used = list_number_used.copy() 
                copy_list_number_used.append(number_test)
                max_sum, list_max_sum, max_lenght, list_max_lenght = recursivity(copy_list_number, copy_list_number_used, max_sum, list_max_sum)

    #No possibility for this branch.

    sum = 0
    for i in list_number_used:
        sum += i
    if sum > max_sum:
        max_sum = sum
        list_max_sum = list_number_used

    if len(list_number_used) > max_lenght:
        max_lenght = len(list_number_used)
        list_max_lenght = list_number_used

    #No egality, it's a future feature 

    return max_sum, list_max_sum, max_lenght, list_max_lenght

def main():
    nb = int(input("Donnez votre nombre \n>>> ")) ###A plus détaillé puis mettre un try pour évité de mettre n'importe quoi.
    list_number = create_list_number(nb) #Create the list of number

    for first_number in list_number:

        #Je retire le chiffre que j'utilise de la liste
        copy_list_number = list_number.copy() #Je fais une copie, pour avoir toujours la liste original complète.
        copy_list_number.pop(first_number-1) #-1 parce que l'array est à 0

        max_sum, list_max_sum, max_lenght, list_max_lenght = recursivity(copy_list_number, list_number_used = [first_number])
        print("sum :", max_sum, list_max_sum)
        print("lenght:", max_lenght, list_max_lenght)

if __name__ == "__main__":
    main()