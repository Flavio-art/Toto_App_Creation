import requests

# Die Anfrage an den Server schicken
response = requests.get('https://official-joke-api.appspot.com/random_joke')

if response.status_code == 200:
    # Die JSON-Antwort in ein Python-Dictionary umwandeln
    joke = response.json()
    print(f"Here's a joke for you: {joke['setup']} - {joke['punchline']}")
else:
    print("Oops! Couldn't fetch a joke.")