import sys

start = sys.stdin.readline().casefold()
special = list(set(start))
if len(special) == 2:
    print(start.capitalize())
else:
    count = [0] * len(special)
    for i in start:
        count[special.index(i)] += 1

    if count.count(max(count)) != 1:
        print("?")
    else:
        print(special[count.index(max(count))].capitalize())

