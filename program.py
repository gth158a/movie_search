from movie_client import MovieClient
import requests.exceptions

def print_header():
    print('--------------------------------------------')
    print('            MOVIE SEARCH APP')
    print('--------------------------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Title search text (x to exit): ')
            if search != 'x':
                client = MovieClient(search)
                # print(client.perform_search())
                results = client.perform_search()
                print('Found {} results.'. format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.Year, r.Title
                    ))
        except requests.exceptions.ConnectionError as ce:
            print('ERROR: Cannot search, your network is down.')
        except ValueError as ve:
            print("ERROR: Your string is invalid: {}".format(ve))
        except Exception as x:
            print("ERROR: {}".format(x))

    print('exiting...')


def main():

    print_header()
    search_event_loop()


if __name__ == '__main__':
    main()

