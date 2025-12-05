id_ranges = []
ingredients = []
merged = []  
finish_ranges= False

with open("input.txt", "r", encoding="utf-8") as f:
   for line in f:
      
      if line != "\n" and not finish_ranges:
         start, end = map(int, line.strip().split("-"))
         id_ranges.append([start, end])
    
      elif finish_ranges:
         ingredients.append(int(line.strip()))

      else:
        finish_ranges = True
         
id_ranges.sort(key=lambda r: r[0])
    

for start, end in id_ranges:
    if not merged:
        merged.append([start, end])
    else:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

total_fresh = sum(end - start + 1 for start, end in merged)


print(total_fresh) 