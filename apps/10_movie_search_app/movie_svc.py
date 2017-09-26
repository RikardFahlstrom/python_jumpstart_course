import requests
import collections

MovieResult = collections.namedtuple('MovieResult',
                                     'imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres')


def find_movies(search_text):

    if not search_text or not search_text.strip():
        raise ValueError("Search text is required")  # If search text is empty or only contains spaces,
    # we create an ValueError which we can call in the exception block

    #  search = input('What do you want to search for? ')
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)
    resp.raise_for_status()  # will raise an error of request is not successful

    movie_data = resp.json()  # since we know that the request is in json-format. Will give us dict-format
    # print(movie_data.keys())  # dict contains 3 keys; 'hits', 'truncated_results' and 'keyword'
    # print(type(movie_data['hits']), movie_data['hits'])  # hits is a list

    movies_list = movie_data.get('hits')

    # print(type(movies), movies)  # need to convert it to something else than a flat list, -> named tuple

    movies = []
    for md in movies_list:
        m = MovieResult(
            imdb_code=md.get('imdb_code'),
            title=md.get('title'),
            duration=md.get('duration'),
            director=md.get('director'),
            year=md.get('year', 0),  # 0 is alternative default value, if no year-info exists, value will be 0
            rating=md.get('rating', 0),
            imdb_score=md.get('imdb_score', 0.0),
            keywords=md.get('keywords'),
            genres=md.get('genres')
        )
        movies.append(m)

        movies.sort(key=lambda m: -m.year)  # using lambda to create sort function for 'm.year'.
          # Since 'm.year' is a numerical value, we can use '-' before to reverse default sort order

    return movies
