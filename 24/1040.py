s = open("24_1040.txt").readline()

max_c = 0
counter = 0
for i in range(len(s)):
    if s[i] not in "1234567890":
        max_c = max(max_c, counter)
        counter = 0
    else:
        counter += 1
print(max_c)