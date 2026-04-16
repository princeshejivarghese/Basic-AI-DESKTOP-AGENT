import webbrowser 
import datetime    

def start_agent():
    # --- PHASE 1: WAKE UP (Outside the loop) ---
    print("--- AI SYSTEM ONLINE ---")
    print("Hello! I am your base agent. What should I do?")

    # --- PHASE 2: RUNNING (The Loop) ---
    while True:
        command = input("\nEnter Command: ").lower()

        if "time" in command:
            now = datetime.datetime.now()
            print(f"The current time is: {now.strftime('%H:%M:%S')}")

        elif "google" in command:
            search = input("What should I search for? ")
            url = f"https://www.google.com/search?q={search}"
            webbrowser.open(url)
            print(f"Opening Google for: {search}")

        elif "youtube" in command:
            search = input("What should I search for? ")
            url = f"https://www.youtube.com/results?search_query={search}"
            webbrowser.open(url)
            print(f"Opening YouTube for: {search}")

        elif "note" in command:
            memo = input("What should I remember? ")
            with open("memory.txt", "a") as file:
                file.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {memo}\n")
            print("Successfully saved to my memory.txt file!")

        elif "exit" in command:
            print("Shutting down... Goodbye!")
            break  

        else:
            print("I don't know that command yet. Teach me more later!")

# --- START THE PROGRAM ---
start_agent()