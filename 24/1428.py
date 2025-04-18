s = open("24_1428.txt").readline()

s = s.replace("XY", "*").replace("XZ", "*")

s2 = s.split("*")
print(sorted(s2, key=lambda x: len(x))[-1])
print(len("YYYYZZYYYYYYYZYYZYZZZXX"))