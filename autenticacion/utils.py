from django.core.cache import cache
import requests

def obtener_paises():
    url = "https://restcountries.com/v3.1/all"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        paises=sorted([(pais['name']['common'], pais['name']['common']) for pais in data])
        print(paises)
        return paises
    except requests.exceptions.RequestException as e:
        print(f"error al obtener paises {e}")
        return []