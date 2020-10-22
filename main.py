from src.Pattern import Pattern
from src.data_writer import DataWriter
dataset = []
for i in range(30):
    dataset.append(Pattern(acnum=i))
DataWriter.file_writer(DataWriter.antigen_data_format(dataset), "data/antigen.tsv")
DataWriter.file_writer(DataWriter.pattern_data_format(dataset), "data/pattern.tsv")

