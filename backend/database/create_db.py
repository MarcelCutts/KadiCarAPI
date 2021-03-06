import sqlite3

con = sqlite3.connect('expenses.db') # creates the file f it doesn't exist yet

con.execute("""CREATE TABLE expenses( 
	id INTEGER PRIMARY KEY, 
	type CHAR(20) NOT NULL, 
	amount REAL NOT NULL,
	date CHAR(10) NOT NULL, 
	mileage INTEGER, 
	litres INTEGER, 
	comment CHAR(100)
)""")

con.commit()