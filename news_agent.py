import requests
from bs4 import BeautifulSoup

def fetch_ai_news():
    print("--- FETCHING LATEST AI NEWS ---")
    url = "https://www.bbc.com/innovation/artificial-intelligence" # A reliable news source
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This logic finds the 'headlines' on the page
        headlines = soup.find_all('h2', limit=5) 
        
        if not headlines:
            return "No headlines found today. Check the URL!"

        print("\nToday's Top AI Stories:")
        for i, head in enumerate(headlines, 1):
            print(f"{i}. {head.get_text().strip()}")
            
        return "\nNews successfully fetched!"
        
    except Exception as e:
        return f"Error: Could not connect to the internet. {e}"

# Run the tool
print(fetch_ai_news())
