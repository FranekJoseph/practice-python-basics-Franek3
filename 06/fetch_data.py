import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Błąd pobierania danych"
print(fetch_data("https://wttr.in/?format=3"))