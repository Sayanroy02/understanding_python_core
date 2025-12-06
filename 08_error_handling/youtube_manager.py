import json


file_name = "youtube.txt"

def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)
        

def list_all_videos(videos):
    print("\nList of all videos:")
    print("*"*50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']} - {video['time']}")
    print("\n")
    print("*"*50) 
def add_video(videos):
    video_title = input("Enter video title: ")
    video_time = input("Enter video time: ")
    videos.append({"title": video_title, "time": video_time})
    save_data_helper(videos)
    

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the sl no. of the video to update: "))
    if 1 <= index <= len(videos):
        video_title = input("Enter video title: ")
        video_time = input("Enter video time: ")
        videos[index-1] = {"title": video_title, "time": video_time}
        save_data_helper(videos)
        print("\nVideo updated successfully")
        list_all_videos(videos)
    else:
        print("Invalid index selected")
    
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the sl no. of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("\nVideo deleted successfully")
        list_all_videos(videos)
    else:
        print("Invalid index selected")


def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager || Choose options")
        print("1. List of all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choices = input("Enter your choice: ")

        match choices:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")
                
if __name__ =="__main__":
    main()

               


