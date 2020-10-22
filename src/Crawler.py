import re
from bs4 import BeautifulSoup
from typing import Optional
import re

class Crawler(object):

    html_regex_strip = '<[^<]+?>'
    @staticmethod
    def return_antigen(soup: BeautifulSoup) -> Optional[list]:
        """
        given a soup, will return the antigens associated with the current page.
        :param soup: parsed file from BeautifulSoup
        :return: string
        """
        label = soup.find("strong", text="Antigen Association")
        label = label.next_element.next_element
        antigen = str(label.next_element)
        antigen = re.sub(Crawler.html_regex_strip, '', antigen)
        if antigen.lower() == "none" or antigen.lower() == "not applicable":
            return None
        antigenlist = re.split(", |/", antigen)
        return antigenlist

    @staticmethod
    def return_previous_nomenclature(soup: BeautifulSoup) -> Optional[list]:
        """
        given a soup, will return a list of all previous nomenclature listed on current page, or None.
        :param soup: parsed file from BeautifulSoup
        :return: list, or None
        """
        label = soup.find("strong", text="Previous Nomenclature")
        label = label.next_element.next_element
        prevnom = str(label.next_element)
        prevnom = re.sub(Crawler.html_regex_strip, '', prevnom)
        if prevnom == "None":
            return None
        prevnomlist = re.split(", |/", prevnom)
        return prevnomlist
    @staticmethod
    def return_description(soup: BeautifulSoup) -> str:
        """
        given a soup, will return the description listed on current page.
        :param soup:
        :return: str
        """
        label = soup.find("strong", text="Description")
        label = label.next_element.next_element
        descp = str(label.next_element)
        descp = re.sub(Crawler.html_regex_strip, '', descp)
        return descp

    @staticmethod
    def return_page_title(soup: BeautifulSoup) -> str:
        """
        given a soup, will return the name of the pattern.
        :param soup:
        :return: str
        """
        label = soup.find(class_="icap-titulo-all").contents
        name = str(label[2].replace("\r", "").strip())
        return name