import requests
from bs4 import BeautifulSoup

headers={
    'Content-Type': 'text/plain; charset=UTF-8',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/board/4',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

def get_one_page(url):
    url = 'https://maoyan.com/board/4'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    names = soup.select('.name > a')
    actors = soup.select('.movie-item-info .star')
    times = soup.select('.movie-item-info .releasetime')
    for name,actor,time in zip(names,actors,times):
        data={
            'name':name.get_text().strip(),
            'actor':actor.get_text().strip(),
            'time': time.get_text().strip()
        }
        print(data)

if __name__=='__main__':
    urls = ['https://maoyan.com/board/4?offset={}'.format(str(i*10)) for i in range(0,10)]
    for url in urls:
        get_one_page(url)