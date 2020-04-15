import requests
from bs4 import BeautifulSoup
import json
import re

def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/80.0.3987.122 Safari/537.36'
        }
    response=requests.get(url,headers=headers)

    soup=BeautifulSoup(response.text,'lxml')

    songs=soup.select('.pc_temp_songlist > ul > li > a')
    times=soup.select('.pc_temp_time ')
    ranks=soup.select('.pc_temp_num')
    for song,time,rank in zip(songs,times,ranks) :
        data={
            'song':song.get_text(),
            'time':time.get_text().strip(),
            'rank':rank.get_text().strip()
        }
        with open('song.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
            f.close()


if __name__=="__main__":
    urls=['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,23)]
    for url in urls:
        get_one_page(url)
