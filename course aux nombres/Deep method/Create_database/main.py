import sqlite3
from recursivity import *

def create_db(nb):
    db = sqlite3.connect(f"../Database/for_{nb}_number.db")
    cur = db.cursor()
    for i in range(1, nb+1, 1):
        cur.execute(f'''CREATE TABLE "{str(i)}"
                (number INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
                total_play INTEGER, 
                victory INTEGER, 
                percent_victory REAL)''')
        
        for j in range(1, nb+1):
            cur.execute(f'''INSERT INTO "{str(i)}" VALUES (?,?,?,?)''', (j, 0, 0, 0))
        db.commit()
    return db

def main():
    nb = int(input("Donnez un nombre \n>>> "))
    create_db(nb)

    list_number = create_list_number(nb) #Create the list of number

    for first_number in list_number:

        #Je retire le chiffre que j'utilise de la liste
        copy_list_number = list_number.copy() #Je fais une copie, pour avoir toujours la liste original complète.
        copy_list_number.pop(first_number-1) #-1 parce que l'array est à 0
        list_number_used= [first_number]
        recursivity(copy_list_number, list_number_used)
        

if __name__ == "__main__":
    main()