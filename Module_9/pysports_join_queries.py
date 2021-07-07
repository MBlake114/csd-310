# Milo Blake
# 07/07/2021
# Module 9.2

#import statements
import mysql.connector
from mysql.connector import errorcode

#database configure object
config = {
    "user": "pysports_user",
    "password": "MySQLpassword!!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
#try block for handling potential MySQL database errors
try:
    db = mysql.connector.connect(**config) #connect to the pysports database

    cursor = db.cursor()

    #Innerjoin query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")

    #loop to display player data 
    for player in players:
        print("  Player ID:  {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0],player[1],player[2],player[3]))

    input("\n\n  Press any key to continue... ")    

#except block to handle errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    #close the connection to MySQL
    db.close()

