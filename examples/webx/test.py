from bs4 import *
from urllib2 import *

if __name__ == '__main__':
    print('test')
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())