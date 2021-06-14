from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://mofanpy.com/static/scraping/table.html").read().decode('utf-8')