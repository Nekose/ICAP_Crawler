import requests
import filecmp
import os
import re
from bs4 import BeautifulSoup
from typing import Optional

class Crawler(object):
    #TODO refactor code to use a ICAP object and store information (name, antigens, etc) inside of it.

    @staticmethod
    def return_antigen(soup: BeautifulSoup) -> str:
        """
        given a soup, will return the antigens associated with the current page.
        :param soup: parsed file from BeautifulSoup
        :return: string
        """
        label = soup.find("strong", text="Antigen Association")
        label = label.next_element.next_element
        antigen = str(label.next_element)
        antigen = antigen.replace("<td>", "").replace("</td>", "")
        return antigen

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
        prevnom = prevnom.replace("<td>", "").replace("</td>", "")
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
        descp = descp.replace("<td>", "").replace("</td>", "").strip()
        return descp

    @staticmethod
    def return_name(soup: BeautifulSoup) -> str:
        """
        given a soup, will return the name of the pattern.
        :param soup:
        :return: str
        """
        label = soup.find(class_="icap-titulo-all").contents
        name = str(label[2].replace("\r", "").strip())
        return name

    @staticmethod
    def crawl_icap():
        tempfile = "temp.tsv"
        outputtable = [["Pattern Name", "Associated Antigens"]]
        for i in range(30):
            url = "https://anapatterns.org/view_pattern.php?pattern=" + str(i)
            print(f"processing {url}")
            page = requests.get(url)
            content = page.content
            soup = BeautifulSoup(content, 'html.parser')
            outputtable.append([Crawler.return_name(soup), Crawler.return_antigen(soup)])
            if Crawler.return_previous_nomenclature(soup) != None:
                prenomlist = Crawler.return_previous_nomenclature(soup)
                for element in prenomlist:
                    outputtable.append([element,Crawler.return_antigen(soup)])

        f = open(tempfile, 'w')
        for element in outputtable:
            f.write("\t".join(element))
            f.write("\n")
        f.close()


        if os.path.isfile("data/ICAPoutputtable.tsv"):
            if filecmp.cmp(tempfile, "data/ICAPoutputtable.tsv", shallow=False) is True:
                print("No Changes since last pull")
                os.remove(tempfile)
            else:
                print("New information found, updating ICAPoutputtable.tsv")
                f = open('data/ICAPoutputtable.tsv', 'w')
                for element in outputtable:
                    f.write("\t".join(element))
                    f.write("\n")
                f.close()
        else:
            print("First run detected, outputting new ICAPoutputtable.tsv")
            if not os.path.exists('data'):
                os.mkdir('data')
            f = open('data/ICAPoutputtable.tsv', 'w')
            for element in outputtable:
                f.write("\t".join(element))
                f.write("\n")
            f.close()
            os.remove(tempfile)

    @staticmethod
    def tableorg():
        data = []
        with open("data/ICAPoutputtable.tsv") as file:
            for line in file:
                line = line.strip("\n")
                lines = line.split("\t")
                if lines[0][0:2] == "AC":
                    data.append(lines[0:2])
        outputdata = [['Pattern Name','Associated Antigens']]
        for line in data[1:]:
            for element in re.split(", |/",line[1]):
                outputdata.append([line[0], element])
        for line in outputdata:
            for pos, element in enumerate(line):
                line[pos] = element.strip(" ")
        f = open('data/ICAPoutputtable2.tsv', 'w')
        for element in outputdata:
            f.write("\t".join(element))
            f.write("\n")
        f.close()