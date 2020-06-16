import requests
from bs4 import BeautifulSoup
import time

def get_title(url,headers):
    response = requests.get(url,headers = headers)
    print(response.status_code)
    time.sleep(2)
    html = response.text

    #print(html)
    soup = BeautifulSoup(html,"lxml")
    h2s = soup.find_all('h2',class_ = "ContentItem-title")
    for h2 in h2s:
        title_href = h2.find('a').get('href')
        title = h2.find('a').text
        print(title +' ' * 7 + "url:" + "https" + title_href )



if __name__ == "__main__":
    base_url = "https://www.zhihu.com/collection/38887091"
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
    #爬取五页的标题
    for i in range(1,5):
        url = base_url + "?page=" + str(i)
        print(' '*20 + '#'*10 + ' '*5 +"开始打印第{}页的内容".format(i) + ' '*5 + '#'*10)
        print(url)
        get_title(url,headers)
        time.sleep(3)
