ways = None  

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        
        
        if ways is None:
            ways = [0] * len(line)
        
       
        if "S" in line:
            s_index = line.index("S")
            ways[s_index] = 1 
       
        next_ways = [0] * len(line)

        for index, char in enumerate(line):
            w = ways[index]
            if w == 0:
                continue  

            if char == "^":
                if index - 1 >= 0:
                    next_ways[index - 1] += w
                if index + 1 < len(line):
                    next_ways[index + 1] += w
            else:
                next_ways[index] += w


        ways = next_ways

total_timelines = sum(ways)
print(total_timelines)
