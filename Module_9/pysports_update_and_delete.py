# Milo Blake
# 07/07/2021
# Module 9.3

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
#method to execute inner join on the player and team tables and display results using for loop
def display_players(cursor,title):
    
    #inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n  -- {} --".format(title))

    #loop to display players
    for player in players:
        print("  Player ID:  {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0],player[1],player[2],player[3]))

#try block for handling potential MySQL database errors
try:
    db = mysql.connector.connect(**config) #connect to the pysports database

    cursor = db.cursor()

    #insert player query
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                  "VALUES('Smeagol', 'Shire Folk', 1)")

    # insert new player
    cursor.execute(add_player)

    #show players in table after insert
    display_players(cursor,"DISPLAYING PLAYERS AFTER INSERT")

    #update player query 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    #update player
    cursor.execute(update_player)

    #show players in table after update
    display_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #delete player query
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    #delete player
    cursor.execute(delete_player)

    #show players in table after delete
    display_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

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