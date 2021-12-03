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

def recursivity(list_number, list_number_used):
    '''
    Test all possibility for find the best sum of all. 

    Requiere:           Type:       Explain: 
    list_number         list        List of number remaining
    list_number_used    list        List of number used, [-1] = the last used.
    '''

    if len(list_number) > 0:
        last = True
        for number_test in list_number:
        
            if number_test > list_number_used[-1]:
                if number_test % list_number_used[-1] == 0:
                    multiple = True
                    last = False
                else:
                    multiple = False
        
            elif number_test < list_number_used[-1]:
                if list_number_used[-1] % number_test == 0:
                    multiple = True
                    last = False
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

    if last==True:
        print(list_number_used)
        db = sqlite3.connect(f"../Database/for_{len(list_number_used)+len(list_number)}_number.db")
        cur = db.cursor()

        try:
            if len(list_number_used) % 2 == 1: #J1 Win
                for i in range(1, len(list_number_used)+1, 1):
                    cur.execute(f"""SELECT * FROM "{str(i)}" WHERE number={list_number_used[i-1]}""")
                    raw_data = cur.fetchone()
                    recup_tolal_play, recup_total_win = int(raw_data[1])+1, int(raw_data[2])+1

                    cur.execute(f"""UPDATE "{str(i)}" SET total_play = ?, victory = ?, percent_victory = ? WHERE number ={list_number_used[i-1]}""", (recup_tolal_play, recup_total_win, (recup_total_win/recup_tolal_play)*100))
                    db.commit()

                
            elif len(list_number_used) % 2 == 0: #J2 Loose
                for i in range(1, len(list_number_used)+1, 1):
                    cur.execute(f"""SELECT * FROM "{str(i)}" WHERE number={list_number_used[i-1]}""")
                    raw_data = cur.fetchone()
                    recup_tolal_play, recup_total_win = int(raw_data[1])+1, int(raw_data[2])

                    cur.execute(f"""UPDATE "{str(i)}" SET total_play = "{recup_tolal_play}", percent_victory = "{(recup_total_win/recup_tolal_play)*100}" WHERE number ={list_number_used[i-1]}""")
                    db.commit()
        except:
            db.commit()
        
