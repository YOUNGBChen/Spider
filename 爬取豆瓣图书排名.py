import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
url = 'https://book.douban.com/tag/2019%E4%B9%A6%E5%8D%95'

def get_one_page(url):
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'lxml')

    names=soup.select('.info > h2 > a')
    writers=soup.select('.info .pub ')

    for name,writer in zip(names,writers):
        data={
            'name':name.get_text().strip().replace('\n',' '),
            'writer':writer.get_text().strip()
        }
        print(data)

if __name__=='__main__':
    urls=['https://book.douban.com/tag/2019%E4%B9%A6%E5%8D%95?start={}'.format(str(i*20)) for i in range(0,4)]
    for url in urls:
        get_one_page(url)