import requests
import movie_svc


def main():
    print_header()
    search_event_loop()


def print_header():
    print('---------------------------')
    print('     MOVIE SEARCH APP')
    print('---------------------------')


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            print()
            search = input("Enter keyword for movie search ('x' to exit): ")
            print()
            if search != 'x':
                result = movie_svc.find_movies(search)
                print("Found {} results.".format(len(result)))
                for r in result:
                    print("{} - {}".format(r.year, r.title))
        except ValueError:  # possible since we raised/defined an ValueError in 'movie_svc'
            print("Error: Search text is required")
        except requests.exceptions.ConnectionError:
            print("Error: Your network is down")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print('exiting...')

if __name__ == '__main__':
    main()


