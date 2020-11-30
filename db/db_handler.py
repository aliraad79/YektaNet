import sqlite3


# initial
connect = sqlite3.connect('yektanet.db')
curser = connect.cursor()

# make tables
curser.execute("CREATE TABLE Ad(id int PRIMARY KEY,title varchar(500) , imgUrl varchar(1000), link varchar(1000), clicks int, views int)")
curser.execute("CREATE TABLE Advertiser(id int PRIMARY KEY,name varchar(500) ,clicks int, views int)")


# Drop tables
# curser.execute("DROP TABLE ADVERTISER")