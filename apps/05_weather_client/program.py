import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport','cond, temp, scale, loc')

def main():
    print_the_header()
    code = input('What zipcode do you want the weather for (97201)? ')
    html = get_html_from_web(code)    # parse the html
    report = get_weather_from_html(html)
    print('The temp in {} is {} {} and {}.'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

def print_the_header():
    print('------------------------------')
    print('          WEATHER APP')
    print('------------------------------')

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    # print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html5lib")

    loc = soup.find(id="location").find("h1").get_text()
    condition = soup.find(id="curCond").find(class_="wx-value").get_text()
    temp = soup.find(id="curTemp").find(class_="wx-value").get_text()
    unit = soup.find(id="curTemp").find(class_="wx-unit").get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_loc(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    unit = cleanup_text(unit)

    #print(condition, temp, unit, loc)
    report = WeatherReport(cond=condition, temp=temp, scale=unit, loc=loc)
    return report

def cleanup_text(text):
    if not text:
        return text
    text = text.strip()
    return text

def find_city_and_state_from_loc(loc : str): # ': str' anger att input kommer alltid vara en str. Detta gör inbyggda "hjälpfunktioner tillgängliga i autocompletion.
    parts = loc.split('\n') # Detta kommer separera texten vid varje nu rad och spara varje del i en lista i 'parts'-variabeln
    return parts[0].strip()


if __name__ == '__main__':
    main()

