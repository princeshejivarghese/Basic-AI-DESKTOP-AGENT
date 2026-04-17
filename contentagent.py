import datetime
import os

def generate_social_bundle(topic):
    print(f"--- CREATING CONTENT BUNDLE FOR: {topic} ---")
    
    # 1. Logic: Generate a 'Video Script'
    script = f"""
    VIDEO SCRIPT: {topic}
    00-05s: Hook - 'Did you know this about {topic}?'
    05-20s: The 'Meat' - Explain the core concept of {topic}.
    20-30s: CTA - 'Follow for more AI & Tech insights!'
    """
    
    # 2. Logic: Generate a 'Poster Idea' (Design side)
    poster_idea = f"POSTER DESIGN: Use a bold neon font. Background: Abstract tech pattern related to {topic}."

    # 3. Hardware Action: Save to a folder
    folder_name = f"Project_{datetime.datetime.now().strftime('%d_%m')}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    with open(f"{folder_name}/bundle.txt", "w") as f:
        f.write(script + "\n\n" + poster_idea)
    
    return f"Bundle created in folder: {folder_name}"

# Start the process
topic_input = input("Enter a topic for your next edit/post: ")
print(generate_social_bundle(topic_input))
