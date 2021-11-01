import sqlite3
from recursivity import *

def create_db(nb):
    db = sqlite3.connect(f"../Database/for_{nb}_number.db")
    cur = db.cursor()
    for i in range(nb): #NB is maximal theoric.
        cur.execute(f'''CREATE TABLE "{str(i)}"
                (number INTEGER PRIMARY KEY, 
                total_play INTEGER, 
                victory INTEGER, 
                percent_victory REAL)''')
            
        for j in range(1,nb+1):
            cur.execute(f'''INSERT INTO "{str(i)}" VALUES (?,?,?,?)''', (j, "NULL", "NULL", "NULL"))

    return db

def main():
    nb = int(input("Donnez un nombre \n>>> "))
    db = create_db(nb)

if __name__ == "__main__":
    main()