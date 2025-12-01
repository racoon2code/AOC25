pos = 50  
zeros = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        dir = line[0]
        dist = int(line[1:])

        old = pos

        if dir == "R":
            pos = old + dist
            
            zeros += pos // 100 - old // 100

        else:  # "L"
            pos = old - dist
            a = pos     
            b = old - 1      
            
            zeros += b // 100 - ((a - 1) // 100)



print(zeros)