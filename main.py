from src.Crawler import Crawler
from src.Pattern import Pattern

patternlist = []
for i in range(2):
    patternlist.append(Pattern('https://anapatterns.org/view_pattern.php?pattern=' + str(i)))

print(patternlist)