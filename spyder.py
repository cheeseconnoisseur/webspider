import random
import multiprocessing
import string
import urllib.request
import bs4 as bs
import requests
url = 'http://arturodezon.me/'
alllinks = ['http://www.bbc.co.uk/news','http://www.bbc.co.uk/news']
n = 0


def locallinks(url, link):
    if not link.startswith('http'):
        return ''.join([url,link])
    else:
        return link

def readpage():
    global n
    n = n + 1
    url = alllinks[n]
    print(url)
    try:
        page = requests.get(url)
    except:
        main()
    soup = bs.BeautifulSoup(page.text, 'lxml')
    body = soup.body
    try:
        links = [link.get('href') for link in body.find_all('a')]
        #print(links)
    except:
        n = n -1
        main()
    #print("lol")
    if len(links) == 0:
        main()
    else:
        try:
            for link in list(links):
                if not isinstance(link, str):
                    #print("not")
                    links.remove(link)
                    continue
                
            links = [str(link.encode("ascii")) for link in links]
            links = [link.replace('b\'','') for link in links]
            links = [link.replace('\'','') for link in links]
            links = [locallinks(url, link) for link in links]
            text = [soup.find_all('p')]
            with open('text.txt', 'a') as f:
                f.write(url + " // " + str(text))
                f.close()
        except:
            main()
            n = n - 1
    return links

def main():
    while True:
        links = readpage()
        alllinks.extend(links)
        random.shuffle(alllinks)

main()
    



#def locallinks():
#    if link.startswith('/'):
#        return ''.join([url,link])
#    else:
#        return link


#page = str(page)
#start = page.index( '<p>' ) + len( '<p>' )
#end = page.index( '</p>', start )
#s = page[start:end]

#links = [locallinks(url, link) for link in links]


##def readpage():
##    global n
##    n = n + 1
##    if n == 1:
##        url = alllinks[n]
##        #url = url[6]
##        print(url)
##        page = requests.get(url)
##        #page = page.read()
##        soup = bs.BeautifulSoup(page.text, 'lxml')
##        body = soup.body
##        links = [link.get('href') for link in body.find_all('a')]
##        links = [str(link.encode("ascii")) for link in links]
##        links = [link.replace('b\'','') for link in links]
##        return links
##    else:
##        url = alllinks[n]
##        #url = url[n]
##        print(url)
##        page = requests.get(url)
##        #page = page.read()
##        soup = bs.BeautifulSoup(page.text, 'lxml')
##        body = soup.body
##        links = [link.get('href') for link in body.find_all('a')]
##        links = [str(link.encode("ascii")) for link in links]
##        links = [link.replace('b\'','') for link in links]
##        return links


