import requests
from bs4 import BeautifulSoup
from pprint import pprint

WEATHER_URL = "https://www.foreca.com"
#city = "dnipro"


def get_city(city):
    param = {
        "q": city,
        "do_search": "Find+place"
    }
    response = requests.post(url=WEATHER_URL, data=param)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup = soup.find("dl", class_="in")
    soup = soup.find_all("dd")
    links = []
    for s in soup:
        link = WEATHER_URL + s.a.get('href')
        links.append(link)
    print(links)
    return links


def weather_data(city_link):
    response = requests.get(url=city_link)
    soup = BeautifulSoup(response.content, 'html.parser' )
    temperature = soup.find("span", class_='cold txt-xxlarge').get_text()
    wind_speed = soup.find("span", class_='cold txt-xxlarge').strong.findNext("strong").get_text()
    info = soup.find("div", class_="right txt-tight").get_text()
    meteogram = soup.find("div", class_="meteogram").img['src']
    meteogram_url = WEATHER_URL + meteogram

    return temperature, wind_speed, info, meteogram_url


def main():
    links = get_city(city="dnipro")
    temperature, wind_speed, info, meteogram_url = weather_data(links[0])
    print(temperature)
    print(wind_speed)
    print (info)
    print(meteogram_url)


if __name__ == "__main__":
    main()