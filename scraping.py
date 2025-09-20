import requests
from bs4 import BeautifulSoup
import time

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

def find_movies():

    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "lxml")
    movies = soup.find_all('li', class_ = "ipc-metadata-list-summary-item")

    for i, movie in enumerate(movies):
        movie_name = movie.find('h3', class_ = 'ipc-title__text ipc-title__text--reduced').text.split('.')[1].strip()
        rate = movie.find('span', class_ = 'ipc-rating-star--rating').text
        rating_ppl = movie.find('span', class_ = 'ipc-rating-star--voteCount').text
        Link = movie.select_one('div div div div div div a')['href']
        base = 'https://www.imdb.com'

        with open(f'movies_scrap/{i}.txt','w') as f:
            f.write(f'🎬Rank {i+1} \n<{movie_name}> \n✨Rating - {rate} \n👩Rated by {rating_ppl} people Link:{base}{Link}\n')

if __name__ == '__main__':
        while True:
             find_movies()
             time_wait = 10
             print(f'Waiting {time_wait} mins...')
             time.sleep(time_wait * 60)
