import sqlite3

def create_db(nb):
    db = sqlite3.connect(f"../Database/for_{nb}_number.db")
    return db

def main():
    nb = int(input("Donnez un nombre \n>>> "))
    db = create_db(nb)

if __name__ == "__main__":
    main()