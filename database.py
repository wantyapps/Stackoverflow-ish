import sqlite3

# menu

print("======WELCOME======")
print("OPTIONS:")
print("1: Show all values")
print("2: Add value to database")
print("Q: exit")
while True:
    options = input(">")

    if options == "1":
        db = sqlite3.connect("dbase.db")
        while True:
            try:
                com = db.execute("""
                SELECT * FROM users
                """)
                for row in com:
                    try:
                        print("VALUE: {}".format(str(row).replace(",", "").replace("'", "").replace("(", "").replace(")", "")))
                    except IndexError:
                        print("Done.")
                        break
                break
            except sqlite3.OperationalError:
                print("Table users not found.")
                print("Adding...")
                db.execute("""CREATE TABLE users (
                    name varchar(255)
                );
                """)
    elif options == "2":
        name = input("NAME>")
        db = sqlite3.connect("dbase.db")
        db.execute("""
        INSERT INTO users (name)
        VALUES ("{}");
        """.format(name))
        db.commit()
        print("Done.")
    elif options == "Q":
        exit(0)
