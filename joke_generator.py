import requests

def fetch_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data['type'] == 'single':
            print(joke_data['joke'])
        else:
            print(f'{joke_data["setup"]} - {joke_data["delivery"]}')
    else:
        print("Failed to retrieve a joke.")

if __name__ == '__main__':
    fetch_joke()