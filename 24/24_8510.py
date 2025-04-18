s = open("24_8510.txt").readline()

s = s.replace("NN", "*").replace("NO", "*").replace("NP", "*")
s = s.replace("PP", "*").replace("PO", "*").replace("PN", "*")
s = s.replace("OO", "*").replace("ON", "*").replace("OP", "*")

s = s.split("*")

print(max([len(c) for c in s]))