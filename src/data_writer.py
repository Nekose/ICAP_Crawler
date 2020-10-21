from src.Pattern import Pattern
from typing import List
import os
import filecmp

class Data_Writer(object):

    @staticmethod
    def antigen_data_format(dataset: List[Pattern]) -> list:
        outputformat = []
        for element in dataset:
            if element.antigens is None:
                continue
            for antigen in element.antigens:
                outputformat.append([antigen, f'{element.acnum} {element.name}'])
        return outputformat

    @staticmethod
    def pattern_data_format(dataset: List[Pattern]) -> list:
        outputformat = []
        for element in dataset:
            if element.antigens is None:
                continue
            else:
                outputformat.append([f'{element.acnum} {element.name}',", ".join(element.antigens)])
            if element.alt_names is None:
                continue
            else:
                for altname in element.alt_names:
                    outputformat.append([altname,", ".join(element.antigens)])
        return outputformat

    @staticmethod
    def file_writer(outputformat: List[str],filename: str, tempfile: str = "tempfile.tsv") -> None:
        f = open(tempfile, 'w')
        for element in outputformat:
            f.write("\t".join(element))
            f.write("\n")
        f.close()

        if not os.path.isfile(filename):
            print("first run detected")
            os.rename(tempfile, filename)
        elif Data_Writer.file_compare(tempfile,filename):
            print("no new changes since last pull")
            os.remove(tempfile)
        else:
            print("Changes since last pull found, writing changelog.txt and updating file")
            with open(tempfile, 'r') as file1:
                with open(filename, 'r') as file2:
                    difference = set(file1).difference(file2)
            difference.discard('\n')

            with open("changelog.txt", 'a') as file_out:
                for line in difference:
                    file_out.write(line)
            os.rename(tempfile, filename)

    @staticmethod
    def file_compare(newfile:str, previousfile: str) -> bool:
        if filecmp.cmp(newfile, previousfile, shallow=False) is True:
            return True
        else:
            return False

