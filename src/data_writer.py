from src.Pattern import Pattern
from typing import List
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
