import sqlite3


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

def recursivity(list_number, list_number_used, db):
    '''
    Test all possibility for find the best sum of all. 

    Requiere:           Type:       Explain: 
    list_number         list        List of number remaining
    list_number_used    list        List of number used, [-1] = the last used. 

    Optional: 
    max_sum             int         The max sum find by the algorithm
    list_max_sum        list        The list of the max sum.

    max_lenght          int         The max lenght find by the algorithm
    list_max_lenght     list        The list of the max lenght
    '''

    if len(list_number) > 0:
        finish = True
        for number_test in list_number:
        
            if number_test > list_number_used[-1]:
                if number_test % list_number_used[-1] == 0:
                    multiple = True
                    finish = False
                else:
                    multiple = False
        
            elif number_test < list_number_used[-1]:
                if list_number_used[-1] % number_test == 0:
                    multiple = True
                    finish = False
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
                recursivity(copy_list_number, copy_list_number_used)

    #No possibility for this branch.
    db = sqlite3.connect(f"../Database/for_4_number.db") ########A delete
    if finish == True:
        if len(list_number_used) %2 !=0: #Impaire = que le joueur 1 gagne
            cur = db.cursor()
            
            


if __name__ == "__main__":
    print("Vous avez pas lancé le bon programme")
