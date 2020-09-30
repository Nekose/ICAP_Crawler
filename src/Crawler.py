import requests
import filecmp
import os
from bs4 import BeautifulSoup

class Crawler(object):
    @staticmethod
    def return_antigen(soup: BeautifulSoup) -> str:
        """
        given a soup, will return the antigens associated with the current page.
        :param soup: parsed file from BeautifulSoup
        :return: string
        """
        label = soup.find("strong", text="Antigen Association")
        label = label.next_element
        label = label.next_element
        antigen = str(label.next_element)
        antigen = antigen.replace("<td>", "")
        antigen = antigen.replace("</td>", "")
        return antigen

    @staticmethod
    def return_name(soup: BeautifulSoup) -> str:
        label = soup.find(class_="icap-titulo-all").contents
        name = str(label[2].replace("\r", "").strip())
        return name

    @staticmethod
    def crawl_icap():
        tempfile = "temp.csv"
        outputtable = [["Pattern Name", "Associated Antigens"]]
        for i in range(30):
            url = "https://anapatterns.org/view_pattern.php?pattern=" + str(i)
            print(f"processing {url}")
            page = requests.get(url)
            content = page.content
            soup = BeautifulSoup(content, 'html.parser')
            outputtable.append([Crawler.return_name(soup), Crawler.return_antigen(soup)])

        f = open(tempfile, 'w')
        for element in outputtable:
            f.write("\t".join(element))
            f.write("\n")
        f.close()

        try:
            if filecmp.cmp(tempfile, "../data/ICAPoutputtable.csv", shallow=False):
                print("No Changes since last pull")
                os.remove(tempfile)
            else:
                print("New information found, updating ICAPoutputtable.csv")
                f = open('/data/ICAPoutputtable.csv', 'w')
                for element in outputtable:
                    f.write("\t".join(element))
                    f.write("\n")
                f.close()
        except FileNotFoundError:
            print("First run detected, outputting new ICAPoutputtable.csv")
            if not os.path.exists('../data/'):
                os.makedirs('../data')
            f = open('../data/ICAPoutputtable.csv', 'w')
            for element in outputtable:
                f.write("\t".join(element))
                f.write("\n")
            f.close()
            os.remove("temp.csv")

    @staticmethod
    def tableorg():
        data = []
        with open("../data/ICAPoutputtable.csv") as file:
            for line in file:
                line = line.strip("\n")
                lines = line.split("\t")
                data.append(lines)
        outputdata = [['Associated Antigens', 'Pattern Name']]

        for line in data[1:]:
            for element in line[1].split(","):
                outputdata.append([line[0], element])
        for line in outputdata:
            for pos, element in enumerate(line):
                line[pos] = element.strip(" ")
        f = open('../data/ICAPoutputtable2.csv', 'w')
        for element in outputdata:
            f.write("\t".join(element))
            f.write("\n")
        f.close()

Crawler.crawl_icap()
Crawler.tableorg()