import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'Title,Poster,Type,imdbID,Year'
)

class MovieClient:
    def __init__(self, search_text):
        self.search_text = search_text

    def perform_search(self):
        search = 'capital'
        url = 'http://www.omdbapi.com/?s={}&y=&plot=short&r=json'.format(
            self.search_text)

        r = requests.get(url)
        data = r.json()

        results = data['Search']

        movies = [
            MovieResult(**m)
            for m in results
            ]

        movies.sort(key=lambda m: m.Title)

        return movies