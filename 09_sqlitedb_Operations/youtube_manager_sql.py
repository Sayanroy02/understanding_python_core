import sqlite3
from tabulate import tabulate   #importing tabulate for better table formatting 

con = sqlite3.connect("ytvideos.db") # connect to the database
cur = con.cursor() # create a cursor object

# create a table
cur.execute("""CREATE TABLE IF NOT EXISTS ytvideos(
            id INTEGER PRIMARY KEY,
            name TEXT,
            time TEXT,
            channel TEXT
            )""")
con.commit() # commit the changes to the database


#methods to perform CRUD operations

def list_all_videos():
    # cur.execute("SELECT * FROM ytvideos")  #here cur is the cursor object which holds the result of the query
    # for row in cur.fetchall():   #fetchall() method fetches all the rows from the result of the query
    #     if len(row)>0:
    #         print(row)
    #     else:
    #         print("No videos found")
    cur.execute("SELECT * FROM ytvideos")
    rows = cur.fetchall()

    if not rows:
        print("\nNo videos found")
        return

    headers = ["ID", "NAME", "TIME", "CHANNEL"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))


def add_video():
    name=input("Enter video name: ")
    time = input("Enter video time: ")
    channel = input("Enter channel name: ")
    
    cur.execute("INSERT INTO ytvideos (name,time,channel) Values (?,?,?)",(name,time,channel))
    con.commit() # commit the changes to the database using connection object
    print("Video added successfully")

def update_video():
    video_id = input("Enter video id to update: ")
    new_name=input("Enter video name: ")
    time = input("Enter video time: ")
    channel = input("Enter channel name: ")

    cur.execute("UPDATE ytvideos SET name=?,time=?,channel=? WHERE id=?",(new_name,time,channel,video_id))
    con.commit() # commit the changes to the database
    print("Video updated successfully")

def delete_video():
    video_id= input("Enter video id to delete: ")
    cur.execute("DELETE FROM ytvideos WHERE id=?",(video_id,)) #here i put , after video_id because it is a tuple
    con.commit() # commit the changes to the database
    print("Video deleted successfully")

def main():
    while True:
        print("\nYoutube Manager || Sql Lite Database")
        print("1. List of all Videoes")
        print("2. Add a Video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        
        #now we need switch cases (here we call it match)
        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                break
            case _:             # default case
                print("Invalid choice")

    con.close()  # close the database connection
    

#running the main function
if  __name__=="__main__":
    main()