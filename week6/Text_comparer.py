import requests

class Text_comparer():

    def __init__(self):
        self = self

    def download(self,url,filename):
        try:
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            return 'Downloaded completed'
        except:
            return 'URL not found'

tc = Text_comparer()

url = 'https://www.gutenberg.org/files/1342/1342-h/1342-h.htm'
filename = 'Jens Peter'
print(tc.download(url, filename))