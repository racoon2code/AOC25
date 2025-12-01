
pos = 50
zeros = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for zeile in f:
        
        if zeile[0] == "L":
            pos = (pos - int(zeile[1:])) % 100
        if zeile[0] == "R":
            pos = (pos + int(zeile[1:])) % 100      
        if pos == 0:
            zeros += 1

print(zeros)