import sqlite3

def create_db():
 con = sqlite3.connect(database=r'Cafe.db')
 cur = con.cursor()

 cur.execute("CREATE TABLE IF NOT EXISTS Order_Info(Order_No INTEGER PRIMARY KEY,Cost Text,Service_charge Text,Tax Text,Subtotal Text,Total Text)")
 cur.execute("CREATE TABLE IF NOT EXISTS Order_Items(Order_No INTEGER PRIMARY KEY,Items Text,Item_qty Text)")
 con.commit()
 cur.close()
 con.close()

create_db()


