import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


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
    #  print(url)
    response = requests.get(url)
    #  print(response.status_code)
    #  print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")

    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_="condition-icon").get_text()
    temp = soup.find(class_="wu-unit-temperature").find(class_="wu-value").get_text()
    unit = soup.find(class_="wu-unit-temperature").find(class_="wu-label").get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_loc(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    unit = cleanup_text(unit)

    #  print(condition, temp, unit, loc)
    report = WeatherReport(cond=condition, temp=temp, scale=unit, loc=loc)

    return report


def cleanup_text(text):
    if not text:
        return text
    text = text.strip()

    return text


def find_city_and_state_from_loc(loc: str):  # ':str' in input variable defines that function input will
    # always be a string. This enables some special string-functionality in the function, like '.split()'
    parts = loc.split('\n')  # This will split the text at each new line, and save each line
    # as a separate input in the 'parts'-variable
    return parts[0].strip()


if __name__ == '__main__':
    main()

