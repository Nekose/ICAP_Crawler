from src.Pattern import Pattern
from src.data_writer import Data_Writer
dataset = []
for i in range(5):
    dataset.append(Pattern('https://anapatterns.org/view_pattern.php?pattern=' + str(i)))
Data_Writer.file_writer(Data_Writer.antigen_data_format(dataset),"data/antigen.tsv")
Data_Writer.file_writer(Data_Writer.pattern_data_format(dataset),"data/pattern.tsv")