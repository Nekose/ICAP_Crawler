from src.Crawler import Crawler
import requests
from bs4 import BeautifulSoup

class Pattern(object):
    def __init__(self,url):
        print(f"processing {url}")
        page = requests.get(url)
        content = page.content
        self.soup = BeautifulSoup(content, 'html.parser')
        self._pagetitle = Crawler.return_page_title(self.soup)
        self.acnum, self.name = self._pagetitle.split(' - ')
        self.antigens = Crawler.return_antigen(self.soup)
        self.alt_names = Crawler.return_previous_nomenclature(self.soup)
        self.description = Crawler.return_description(self.soup)

    def __str__(self):
        return f"Pattern object for {self.acnum}, {self.name}"

    def __repr__(self):
        return self.acnum