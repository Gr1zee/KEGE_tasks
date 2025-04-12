data = open("17_21416.txt").read().splitlines()
data = [int(x) for x in data]

suma_otr = 0
c = 0
maximum = 0

for elem in data:
    if elem < 0:
        suma_otr += elem

print(suma_otr)
        

for i in range(len(data)-2):
    nums = data[i], data[i+1], data[i+2]
    if max(nums) * min(nums) > suma_otr:
        c += 1
        maximum = max(sum(nums), maximum)
print(c, maximum)