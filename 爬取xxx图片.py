from bs4 import BeautifulSoup
import urllib.request
import threading
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}
link = []


def test2(x):
    url = 'https://www.meizitu.com/a/list_1_' + str(x) + '.html'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    pictures = soup.select('.pic ')
    for picture in pictures:
        link.append(picture.find('img')['src'])


def test(link, a):
    path = r'D:/111/' + str(a) + '.jpg'
    urllib.request.urlretrieve(link, path)


pool1 = []
for i in range(1, 94):
    th = threading.Thread(target=test2, args=(i,))
    pool1.append(th)
for i in pool1:
    i.start()
for th in pool1:
    threading.Thread.join(th)
print('创建完毕')

pool = []
a = 0
for i in range(len(link)):
    th = threading.Thread(target=test, args=(link[i], a))
    pool.append(th)
    a += 1

for c in range(30):
    count = c * 100
    for i in pool[count:count + 100]:
        i.start()
    for th in pool[count:count + 100]:
        threading.Thread.join(th)
    print('第' + str(c) + '批完成')

