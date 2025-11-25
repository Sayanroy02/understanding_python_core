import time

max_retries = 5
wait_time = 1
attempt = 0


while attempt < max_retries:
    print("Attempts" , attempt + 1 ,"- Wait time" , wait_time )
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1
    
print("Max retries reached. Exiting.")
    
