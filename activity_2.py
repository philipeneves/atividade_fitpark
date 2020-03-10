from bs4 import BeautifulSoup
import requests

def airportData():
    try:
        code = input("Por favor, insira o código ICAO:")
        html = requests.get("https://www.aisweb.aer.mil.br/?i=aerodromos&codigo=" + code)
        soup = BeautifulSoup(html.content, "html.parser")
        airport_name = soup.find('div', {"class":"col-lg-8"}).findNext("h1")
        sunrise = soup.find('sunrise')
        sunset = soup.find('sunset')
        metar = soup.find('h5',{"class":"mb-0 heading-primary"}).findNext("p")
        taf = soup.find('h5',{"class":"mb-0 heading-primary"}).findNext("p").findNext("p")
        list_letters = soup.find_all('a', href=True, attrs={'onclick':"javascript:pageTracker._trackPageview('/cartas/aerodromos');"})
        print("Olá, aviador!\nHoje o sol nasceu às", sunrise.text + ", e irá se pôr às", sunset.text + ".\nSeguem abaixo outras informações sobre o aeroporto", airport_name.text)

        print("\nCartas:\n")
        for list in list_letters:
            print(f"{list.get_text()}")
        print("Metar:\n",metar.text)
        print("Taf:\n",taf.text)
    except:
        print("Informações sobre este aeroporto não foram encontradas, favor verificar o código ICAO.")
    

airportData()