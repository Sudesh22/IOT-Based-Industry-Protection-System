import sqlite3

def delete_table(name):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("DROP TABLE " + name)
    conn.commit()
    conn.close()

delete_table("loginDetails")
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS loginDetails(
                id integer primary key,
                name text,
                email text,
                password text)
            """)
c.execute("INSERT INTO loginDetails VALUES (?,?,?,?)", (1,"abc","abc@gmail.com","abc@123"))
conn.commit()
conn.close()
