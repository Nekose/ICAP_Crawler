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
        antigen = antigen.replace("<td>","")
        antigen = antigen.replace("</td>", "")
        return antigen

    @staticmethod
    def return_name(soup: BeautifulSoup) -> str:
        label = soup.find(class_="icap-titulo-all").contents
        name = str(label[2].replace("\r", "").strip())
        return(name)

page = requests.get("https://anapatterns.org/view_pattern.php?pattern=")
content = page.content
soup = BeautifulSoup(content,'html.parser')

outputtable = [["Pattern Name","Associated Antigens"]]
for i in range(30):
    url = "https://anapatterns.org/view_pattern.php?pattern=" + str(i)
    print(f"processing {url}")
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content,'html.parser')
    outputtable.append([Crawler.return_name(soup),Crawler.return_antigen(soup)])

f = open('temp.csv', 'w')
for element in outputtable:
    f.write("\t".join(element))
    f.write("\n")
f.close()



try:
    if filecmp.cmp("temp.csv","../data/ICAPoutputtable.csv",shallow=False):
        print("No Changes since last pull")
        os.remove("temp.csv")
    else:
        print("New information found, updating ICAPoutputtable.csv")
        f = open('/data/ICAPoutputtable.csv', 'w')
        for element in outputtable:
            f.write("\t".join(element))
            f.write("\n")
        f.close()
except:
    print("First run detected, outputting new ICAPoutputtable.csv")
    f = open('../data/ICAPoutputtable.csv', 'w')
    for element in outputtable:
        f.write("\t".join(element))
        f.write("\n")
    f.close()
    os.remove("temp.csv")