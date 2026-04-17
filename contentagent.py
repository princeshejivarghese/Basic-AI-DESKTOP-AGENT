import datetime
import os
import psutil  # The Hardware Bridge

def check_system_health():
    # 1. Check Battery
    battery = psutil.sensors_battery()
    percent = battery.percent if battery else 100
    
    # 2. Check CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    print(f"--- SYSTEM CHECK: Battery: {percent}% | CPU: {cpu_usage}% ---")
    
    # Logic: Safety First
    if percent < 20 and not battery.power_plugged:
        return False, "Low Battery! Plug in your charger before automating."
    if cpu_usage > 85:
        return False, "CPU is too hot/busy. Wait a moment."
    
    return True, "System Healthy"

def generate_social_bundle(topic):
    # RUN THE HARDWARE CHECK FIRST
    healthy, message = check_system_health()
    if not healthy:
        return f"ERROR: {message}"

    print(f"--- CREATING CONTENT BUNDLE FOR: {topic} ---")
    
    # Logic: Generate Script & Poster Idea
    script = f"VIDEO SCRIPT: {topic}\nHook: 'The future of {topic} is here!'"
    poster_idea = f"POSTER: Tech-minimalist style for {topic}."

    # Folder Creation
    folder_name = f"Project_{datetime.datetime.now().strftime('%d_%m_%H%M')}"
    os.makedirs(folder_name, exist_ok=True)
    
    with open(f"{folder_name}/bundle.txt", "w") as f:
        f.write(script + "\n\n" + poster_idea)
    
    return f"Success! Bundle saved in {folder_name}"

# Execution
topic_input = input("Enter a topic: ")
print(generate_social_bundle(topic_input))