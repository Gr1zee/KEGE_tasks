N = 6666
data = list(map(int, open("26_838.txt").read().splitlines()))
data.sort()

disk_max = []
disk_min = []

i = 0
j = len(data) - 1
while i <= j:
    if sum(disk_max) >= sum(disk_min):
        disk_min.append(data[i])
        i += 1
    else:
        disk_max.append(data[j])
        j -= 1

print(len(disk_max), len(disk_min))
