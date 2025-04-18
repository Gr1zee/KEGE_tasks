s = open("24_4602.txt").readline()

s = s.replace("BA", "*").replace("BO", "*").replace("CA", "*").replace("CO", "*").replace("DA", "*").replace("DO", "*")

s = s.replace("A", " ").replace("B", " ").replace("C", " ").replace("D", " ").replace("O", " ")

print(max([len(c) for c in s.split()]))