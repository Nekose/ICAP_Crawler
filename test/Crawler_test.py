import unittest
from src.Crawler import Crawler
from bs4 import BeautifulSoup

class Test_crawler(unittest.TestCase):
    def setUp(self) -> None:
        self.html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>

        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>

        <p class="story">...</p>
        """
        self.testsoup = BeautifulSoup(self.html_doc,"html.parser")

    def test_something(self):
        print(self.testsoup.head)
        print(self.testsoup.a)


if __name__ == '__main__':
    unittest.main()
