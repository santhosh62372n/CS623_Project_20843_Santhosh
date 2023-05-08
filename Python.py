import psycopg2
from tabulate import tabulate

con = psycopg2.connect(
    host="localhost",
    database="CS623_Project",
    user="postgres",
    password="3303")
    print(con)
    
#For isolation: SERIALIZABLE
con.set_isolation_level(3)
#For atomicity
con.autocommit = False

#1.The product p1 is deleted from Product and Stock.

try:
    cur = con.cursor()
    cur.execute("DELETE FROM product WHERE prodid = 'p1'")

    
except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")
        
 #3. The product p1 changes its name to pp1 in Product and Stock.
 
 #For isolation: SERIALIZABLE
con.set_isolation_level(3)
#For atomicity
con.autocommit = False
cur = con.cursor()

try:
    cur = con.cursor()
    cur.execute("UPDATE Product SET prodid = 'pp1' WHERE prodid = 'p1'")

except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:


    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")
        
#5.We add a product (p100, cd, 5) in Product and (p100, d2, 50) in Stock.

try:
    cur = con.cursor()
    cur.execute("INSERT INTO Product (prodid, pname, price) VALUES ('p100', 'cd', 5)")
    cur.execute("INSERT INTO Stock (prodid, depid, quantity) VALUES ('p100', 'd2', 50)")
    
except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")
