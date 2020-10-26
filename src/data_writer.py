from src.Pattern import Pattern
from typing import List
import os
import filecmp
from datetime import datetime

class DataWriter(object):

    @staticmethod
    def antigen_data_format(dataset: List[Pattern]) -> list:
        """
        Takes a list of pattern objects, and returns a list of antigen -> pattern associations
        :param dataset: list of pattern objects
        :return: list of strings
        """
        outputformat = []
        for element in dataset:
            if element.antigens is None:
                continue
            for antigen in element.antigens:
                outputformat.append([antigen, f'{element.acnum} {element.name}'])
        return outputformat

    @staticmethod
    def pattern_data_format(dataset: List[Pattern]) -> list:
        """
        Takes a list of pattern objects, and returns a list of pattern name -> antigen associations
        :param dataset: list of pattern objects
        :return: list of strings
        """
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
        """
        accepts a list of strings created from pattern_data_format or antigen_data_format, and creates a .tsv
        file ready to be read by excel. If filename is the same as a previously existing file,
        will compare for changes. If no new changes detected, will notify, if changes since last run will produce a
        changelog when overwriting.
        :param outputformat: list of strings output from pattern_data_format or antigen_data_format
        :param filename: desired name of file
        :param tempfile: optional name of tempfile, defaults to tempfile.tsv
        :return: None
        """
        dt = datetime.now()
        if not os.path.isdir("data"):
            print("Creating data directory")
            os.mkdir("data")

        f = open(tempfile, 'w')
        for element in outputformat:
            f.write("\t".join(element))
            f.write("\n")
        f.close()

        if not os.path.isfile(filename):
            print(f"First run, creating {filename} without comparing to previous run.")
            os.rename(tempfile, filename)
        elif DataWriter.file_compare(tempfile, filename):
            print(f"No new changes to {filename} since last pull")
            os.remove(tempfile)
        else:
            print(f"Changes to {filename} since last pull found, writing changelog.txt and updating file")
            with open(tempfile, 'r') as file1:
                with open(filename, 'r') as file2:
                    difference = set(file1).symmetric_difference(file2)
            difference.discard('\n')

            with open("changelog.txt", 'a') as file_out:
                file_out.write("\n" + str(dt) + ":\n")
                for line in difference:
                    file_out.write(line)
            os.rename(tempfile, filename)

    @staticmethod
    def file_compare(newfile:str, previousfile: str) -> bool:
        """
        compares two files for differences
        :param newfile: file name in current working directory
        :param previousfile: file name in current working directory
        :return: True if files are same, False if different
        """
        if filecmp.cmp(newfile, previousfile, shallow=False) is True:
            return True
        else:
            return False

