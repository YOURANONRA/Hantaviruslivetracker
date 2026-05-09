import json
import requests
from datetime import datetime

def fetch_latest_data():
    # In a real scenario, you would fetch from a health API
    # For now, we simulate an update based on 2026 outbreak trends
    
    # Example: Increase cases by a random small margin to simulate "Live" tracking
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Logic: Auto-increment or fetch from a source
    # data['confirmedCases'] += 1 
    
    # Update the timestamp to the current time (IST)
    now = datetime.now()
    data['lastUpdated'] = now.strftime("%B %d, %2026 - %H:%M IST")

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    fetch_latest_data()
