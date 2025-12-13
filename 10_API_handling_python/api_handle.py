import requests
import json

#function to fetch single user data from freeapi

def fetch_users_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    headers = {"accept": "application/json"}
    querystring = {"page":"1","limit":"5"}
    response = requests.get(url,headers=headers , params=querystring)
    user_data = response.json()
    #how to extract data from user_data only one data
    if user_data["success"] and "data" in user_data:
        user_info = user_data["data"]["data"]
        first_user = user_info[0]
        username =first_user["login"]["username"]
        user_location = first_user["location"]["country"]
        return username , user_location
    else:
        raise Exception("Failed to fetch user data")  #raise is used to raise an exception
    
#fetch all users    

def fetch_all_users_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    headers = {"accept": "application/json"}
    querystring = {"page":"1","limit":"5"}
    response = requests.get(url,headers=headers , params=querystring)
    user_data = response.json()
    #how to extract data from user_data only one data
    if user_data["success"] and "data" in user_data:
        users_list = []
        for user in user_data["data"]["data"]:
            usernames = user["login"]["username"]
            user_locations = user["location"]["country"]
            users_list.append((usernames, user_locations))
            
        return users_list
    else:
        raise Exception("Failed to fetch user data")  #raise is used to raise an exception   
 
#function to handle user options 
   
def user_fetch_option():
    while True:
        print("User Data Fetch Options")
        print("1. Fetch Single User Data")
        print("2. Fetch All User Data")
        print("3. Exit")
        choice = input("Enter your choice: ")
    
        match choice:
            case "1":
                username, user_location = fetch_users_freeapi()
                print(f"Username: {username}, Location: {user_location}")
            case "2":
                users = fetch_all_users_freeapi()
                for username, user_location in users:
                    print(f"Username: {username}, Location: {user_location}")
            case "3":
                break
            case _:
                print("Invalid choice")
    
   
    
def main():
    try:
        user_fetch_option()
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()