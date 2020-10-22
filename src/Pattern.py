from src.Crawler import Crawler
import requests
from bs4 import BeautifulSoup

class Pattern(object):
    """
    pattern object to store data pulled from ICAP website. Each object represents an ICAP standard pattern, and
    retains information regarding its name, alternate name, AC number, associated antigens, and pattern description.
    """
    def __init__(self, url: str = None, acnum: int = None):
        """
        accepts a url matching ICAP pattern page, IE https://anapatterns.org/view_pattern.php?pattern=0
        optionally takes raw AC number as an int.
        :param url: url string
        :param acnum: Int of AC number
        """
        if acnum != None:
            url = 'https://anapatterns.org/view_pattern.php?pattern=' + str(acnum)
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