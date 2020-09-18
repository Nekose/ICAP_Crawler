data = []
with open("../data/ICAPoutputtable.csv") as file:
    for line in file:
        line = line.strip("\n")
        lines = line.split("\t")
        data.append(lines)
print(data)
outputdata = [['Associated Antigens','Pattern Name']]

for line in data[1:]:
    for element in line[1].split(","):
        outputdata.append([line[0],element])
for line in outputdata:
    for pos,element in enumerate(line):
        line[pos] = element.strip(" ")
print(outputdata)
f = open('../data/ICAPoutputtable2.csv', 'w')
for element in outputdata:
    f.write("\t".join(element))
    f.write("\n")
f.close()