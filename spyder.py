import random
import multiprocessing
import string
import urllib.request
import bs4 as bs
import requests
inp = input("enter site: www.blahdiblah.com###example:http://www.businessinsider.com/flashback-this-is-what-the-first-website-ever-looked-like-2011-6 ## type bi for latter example   ")

if inp == 'bi':
    inp = 'http://www.businessinsider.com/flashback-this-is-what-the-first-website-ever-looked-like-2011-6'
elif not inp.startswith('http'):
        inp = ('https://' + inp)
url = inp
alllinks = []
alllinks.append(url)
alllinks.append(inp)
#alllinks = ['http://www.bbc.co.uk/news','http://www.bbc.co.uk/news']
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

#links = [locallinks(url, link) for link in links]it

