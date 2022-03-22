import bs4
import requests

r = requests.get('https://www.cphbusiness.dk/')
r.raise_for_status()

soup = bs4.BeautifulSoup(r.text, 'html.parser')


for link in soup.select('a'):
    if link.get('href') and link.get('href').startswith('https'):
        print(link.get('href'))
        open('links', 'a').write(link.get('href')+'\n')
        ri = requests.get(link.get('href'))
        ri.raise_for_status()
        try:
            soupi = bs4.BeautifulSoup(r.text, 'html.parser')
            for link in soupi.select('a'):
                if link.get('href') and link.get('href').startswith('https'):
                    print(link.get('href'))
                    open('link in links', 'a').write(link.get('href')+'\n')
        except:
            print('Log it required')
