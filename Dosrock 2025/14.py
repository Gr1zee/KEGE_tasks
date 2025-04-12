for x in "0123456789ABCDEFGHIJK":
    n1 = f"82934{x}2"
    n2 = f"2924{x}{x}7"
    n3 = f"67564{x}8"
    r = int(n1, 21) + int(n2, 21) + int(n3, 21)
    if r % 20 == 0:
        print(r//20)