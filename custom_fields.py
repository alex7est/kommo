from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

ACCESS_TOKEN = os.getenv("KOMMO_ACCES_TOKEN")
url = "https://teccomcuenca.kommo.com/api/v4/leads/custom_fields"

headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

response = requests.get(url, headers=headers)

obj:dict

# Recuperar los campos de los leads creados por el usuario

try:
    data = json.loads(response.text)
    
    # Extract custom fields from _embedded
    custom_fields = data.get('_embedded', {}).get('custom_fields', [])
    
    # Filter objects based on the specified conditions
    filtered_objects = [
        obj for obj in custom_fields 
        if obj.get('is_deletable') is True and obj.get('is_predefined') is False
    ]
    
    for obj in filtered_objects:
        # Get the first 3 items from the object        
        limited_obj = dict(list(obj.items())[:3])
        print(json.dumps(limited_obj, indent=2))

except Exception as e:
    print(f"An error occurred: {e}")