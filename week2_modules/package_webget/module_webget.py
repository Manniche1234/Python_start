from notebooks.modules import webget
import os
import urllib.request as req
from urllib.parse import urlparse


url = "https://mathshistory.st-andrews.ac.uk/HistTopics/1000_places/"
    
webget.download(url)



